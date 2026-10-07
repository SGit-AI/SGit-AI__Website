"""newsroom.py — the editorial layer over the articles: who places what, where, and why.

The rule underneath is still the one in content.py: PUBLISHING IS ADDING ONE FILE. An agent
that writes admin/content/articles/<slug>.md has published an article: it is live at its
URL, at the top of Latest, in the archive, the feed and the wire, the moment the build runs.
Nobody has to approve it and no shared file has to be edited, so no agent waits on another.

What this module adds is PLACEMENT, and placement has exactly one owner. The lead, the
highlights, the homepage band and the collections featured on the front are decided by the
Editor, in one file, admin/content/newsroom/front.json. Every other agent can ASK for a
placement by adding a pitch (one file, append-only) and the Editor answers it by editing
the pitch's `status` line. Many writers, one owner: the same shape as the inbox, where
every agent may write a draft and one agent maintains the drafts.

Layout (all under admin/content/newsroom/):

    front.json                                   the front page. Editor only.
    roles/<slug>.md                              one desk role per file, with its write policy
    collections/<id>.md                          a curated set of articles with an intro
    notes/YYYY/MM/DD/<slug>.md                   desk notes: nuggets, threads, weeklies
    pitches/YYYY-MM-DD__<slug>.md                a request for placement. Anyone; append-only
    board/<id>-<slug>.md                         the desk's kanban, one card per file
    log/YYYY/MM/DD/<HHMM>__<role>__<slug>.md     one record per desk run. Append-only

A placement that names an article which does not exist (renamed, held back) does NOT fail
the build. A contributor's rename must never be blocked by a file only the Editor may edit,
so the placement is dropped, the slot falls back to the newest article, and the finding is
printed by the build and shown on /newsroom/ under Desk health until the Editor fixes it.
"""
import fnmatch
import json
import os
import re

from content import Content_Error

RE_DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
RE_SLUG = re.compile(r'^[a-z0-9][a-z0-9\-]*$')

NOTE_KINDS = {
    'nugget':   'Nugget',      # one line from an article, and why it matters
    'thread':   'Thread',      # a connection across articles that none of them states
    'weekly':   'The week',    # what was published, what it adds up to
    'brief':    'Brief',       # a short piece written from the data behind the articles
    'correction': 'Correction',
}
BOARD_STATUS = ['backlog', 'doing', 'review', 'done']
PITCH_ASKS = {'lead', 'highlight', 'homepage', 'collection', 'note'}
PITCH_STATUS = {'open', 'accepted', 'declined', 'parked'}
MAX_HIGHLIGHTS = 4
LEAD_STALE_DAYS = 3   # a lead older than this, with newer unplaced articles, is flagged


def _list(v):
    return [x.strip() for x in (v or '').split(',') if x.strip()]


class Newsroom:
    """Loads and validates the newsroom files. Structural errors (bad frontmatter, a date
    that disagrees with its folder, a duplicate slug) fail the build, like everything else
    here; references to articles that do not exist are findings, not failures."""

    def __init__(self, loader, content_root, articles):
        self.L = loader
        self.root = os.path.join(content_root, 'newsroom')
        self.articles = articles
        self.by_slug = {a['slug']: a for a in articles}
        self.findings = []          # (level, where, text) — rendered as Desk health
        self.front = self._load_front()
        self.roles = self._load_roles()
        self.collections = self._load_collections()
        self.notes = self._load_notes()
        self.pitches = self._load_pitches()
        self.board = self._load_board()
        self.log = self._load_log()

    # ------------------------------------------------------------------ helpers

    def _find(self, level, where, text):
        self.findings.append((level, where, text))

    def _md(self, path, where):
        with open(path) as f:
            return self.L.parse_frontmatter(f.read(), where)

    def _walk(self, sub):
        base = os.path.join(self.root, sub)
        out = []
        for d, _dirs, files in os.walk(base):
            for fn in files:
                if fn.endswith('.md') and fn != 'README.md':
                    full = os.path.join(d, fn)
                    out.append((full, os.path.relpath(full, os.path.dirname(self.root))))
        return sorted(out)

    def _article(self, slug, where):
        if slug in self.by_slug:
            return slug
        self._find('warn', where, f'names article {slug!r}, which is not published; the placement is skipped')
        return None

    # ------------------------------------------------------------------ front.json

    def _load_front(self):
        path = os.path.join(self.root, 'front.json')
        where = 'newsroom/front.json'
        if not os.path.exists(path):
            return {'edition': '', 'editor': '', 'note': '', 'lead': None, 'highlights': [],
                    'homepage': {}, 'collections': [], 'off_latest': []}
        try:
            with open(path) as f:
                fr = json.load(f)
        except ValueError as e:
            raise Content_Error(f'{where}: not valid JSON ({e})')
        if fr.get('edition') and not RE_DATE.match(fr['edition']):
            raise Content_Error(f'{where}: edition must be YYYY-MM-DD')

        def slot(x, name):
            if not x:
                return None
            if isinstance(x, str):
                x = {'slug': x}
            s = self._article(x.get('slug', ''), f'{where} {name}')
            return dict(x, slug=s) if s else None

        lead = slot(fr.get('lead'), 'lead')
        highs = [h for h in (slot(x, f'highlights[{i}]') for i, x in enumerate(fr.get('highlights', []))) if h]
        if lead:
            highs = [h for h in highs if h['slug'] != lead['slug']]
        if len(highs) > MAX_HIGHLIGHTS:
            self._find('warn', where, f'{len(highs)} highlights; the front shows the first {MAX_HIGHLIGHTS}')
            highs = highs[:MAX_HIGHLIGHTS]
        off = [s for s in fr.get('off_latest', []) if self._article(s, f'{where} off_latest')]
        return {
            'edition': fr.get('edition', ''), 'editor': fr.get('editor', ''), 'note': fr.get('note', ''),
            'lead': lead, 'highlights': highs, 'homepage': fr.get('homepage', {}),
            'collections': fr.get('collections', []), 'off_latest': off,
        }

    # ------------------------------------------------------------------ roles = policies

    def _load_roles(self):
        roles = []
        for full, where in self._walk('roles'):
            meta, body = self._md(full, where)
            self.L._require(meta, ['title', 'order', 'mission', 'claim', 'owns', 'writes', 'never'], where)
            r = dict(meta)
            r.update({'slug': os.path.basename(full)[:-3], 'body': body, 'where': where,
                      'order': int(meta['order']), 'writes': _list(meta['writes']),
                      'edits': _list(meta.get('edits', '')), 'reads': _list(meta.get('reads', ''))})
            roles.append(r)
        roles.sort(key=lambda r: r['order'])
        return roles

    def role(self, slug):
        return next((r for r in self.roles if r['slug'] == slug), None)

    def may_write(self, role_slug, path):
        """The behaviour policy as a function: may this role create or change this path?
        `writes` is what the role owns or adds; `edits` is the narrower set of other
        roles' files it may change one line in (the Editor's pitch `status`). The
        policy checker uses this; nothing at build time can know who wrote a file."""
        r = self.role(role_slug)
        if not r:
            return False, 'no such role'
        for g in r['writes']:
            if fnmatch.fnmatch(path, g):
                return True, f'writes {g}'
        for g in r['edits']:
            if fnmatch.fnmatch(path, g):
                return True, f'edits {g} (status lines only)'
        return False, 'outside the role\'s write policy'

    # ------------------------------------------------------------------ collections

    def _load_collections(self):
        cols = []
        for full, where in self._walk('collections'):
            meta, body = self._md(full, where)
            self.L._require(meta, ['title', 'dek', 'curator', 'articles', 'updated'], where)
            if not RE_DATE.match(meta['updated']):
                raise Content_Error(f'{where}: updated must be YYYY-MM-DD')
            slugs = [s for s in _list(meta['articles']) if self._article(s, where)]
            cols.append(dict(meta, id=os.path.basename(full)[:-3], body=body, where=where,
                             slugs=slugs, order=int(meta.get('order', 50))))
        cols.sort(key=lambda c: (c['order'], c['title']))
        ids = {c['id'] for c in cols}
        for cid in self.front['collections']:
            if cid not in ids:
                self._find('warn', 'newsroom/front.json collections', f'names collection {cid!r}, which has no file')
        return cols

    # ------------------------------------------------------------------ notes

    def _dated(self, full, where, meta, key='date'):
        m = re.search(r'/(\d{4})/(\d{2})/(\d{2})/', full)
        if not RE_DATE.match(meta.get(key, '')):
            raise Content_Error(f'{where}: {key} must be YYYY-MM-DD')
        if m and '-'.join(m.groups()) != meta[key]:
            raise Content_Error(f'{where}: {key} {meta[key]} does not match its folder {"-".join(m.groups())}')

    def _load_notes(self):
        notes, seen = [], set()
        for full, where in self._walk('notes'):
            meta, body = self._md(full, where)
            self.L._require(meta, ['title', 'date', 'kind', 'role', 'summary'], where)
            self._dated(full, where, meta)
            if meta['kind'] not in NOTE_KINDS:
                raise Content_Error(f'{where}: kind must be one of {sorted(NOTE_KINDS)}')
            slug = os.path.basename(full)[:-3]
            if slug in seen:
                raise Content_Error(f'{where}: duplicate note slug {slug!r}')
            seen.add(slug)
            if meta.get('status', 'published') != 'published':
                continue
            cites = [s for s in _list(meta.get('cites', '')) if self._article(s, where)]
            notes.append(dict(meta, slug=slug, body=body, where=where, cites=cites))
        notes.sort(key=lambda n: (n['date'], n['slug']), reverse=True)
        return notes

    # ------------------------------------------------------------------ pitches

    def _load_pitches(self):
        out = []
        for full, where in self._walk('pitches'):
            meta, body = self._md(full, where)
            self.L._require(meta, ['date', 'from', 'ask', 'article', 'status'], where)
            if not RE_DATE.match(meta['date']):
                raise Content_Error(f'{where}: date must be YYYY-MM-DD')
            if meta['ask'] not in PITCH_ASKS:
                raise Content_Error(f'{where}: ask must be one of {sorted(PITCH_ASKS)}')
            if meta['status'] not in PITCH_STATUS:
                raise Content_Error(f'{where}: status must be one of {sorted(PITCH_STATUS)}')
            out.append(dict(meta, slug=os.path.basename(full)[:-3], body=body, where=where,
                            known=meta['article'] in self.by_slug))
        out.sort(key=lambda p: (p['date'], p['slug']), reverse=True)
        return out

    # ------------------------------------------------------------------ board + log

    def _load_board(self):
        cards = []
        for full, where in self._walk('board'):
            meta, body = self._md(full, where)
            self.L._require(meta, ['title', 'id', 'status', 'role', 'opened'], where)
            if meta['status'] not in BOARD_STATUS:
                raise Content_Error(f'{where}: status must be one of {BOARD_STATUS}')
            cards.append(dict(meta, body=body, where=where))
        cards.sort(key=lambda c: (c['opened'], c['id']))
        return cards

    def _load_log(self):
        runs = []
        for full, where in self._walk('log'):
            meta, body = self._md(full, where)
            self.L._require(meta, ['date', 'time', 'role', 'title'], where)
            self._dated(full, where, meta)
            runs.append(dict(meta, body=body, where=where, slug=os.path.basename(full)[:-3]))
        runs.sort(key=lambda r: (r['date'], r['time']), reverse=True)
        return runs

    # ------------------------------------------------------------------ derived

    def lead(self):
        """The lead: the Editor's pick, or the newest article while there is none."""
        if self.front['lead']:
            return self.front['lead']
        return {'slug': self.articles[0]['slug'], 'kicker': 'Latest', 'why': ''} if self.articles else None

    def placed(self):
        s = set()
        if self.front['lead']:
            s.add(self.front['lead']['slug'])
        s |= {h['slug'] for h in self.front['highlights']}
        for c in self.collections:
            s |= set(c['slugs'])
        return s

    def latest(self, n=None):
        off = set(self.front['off_latest'])
        xs = [a for a in self.articles if a['slug'] not in off]
        return xs[:n] if n else xs

    def placement_of(self, slug):
        out = []
        if self.front['lead'] and self.front['lead']['slug'] == slug:
            out.append('lead')
        if any(h['slug'] == slug for h in self.front['highlights']):
            out.append('highlight')
        out += [f'collection:{c["id"]}' for c in self.collections if slug in c['slugs']]
        return out

    def health(self, has_graph, has_card):
        """The Editor's checklist, computed. Printed by admin/build/desk.py, shown on
        /newsroom/, and the first thing an Editor run reads."""
        out = list(self.findings)
        lead = self.lead()
        placed = self.placed()
        if not self.front['lead']:
            out.append(('warn', 'front.json', 'no lead is set; the newest article is leading by default'))
        elif self.articles:
            import datetime as _dt
            ld = self.by_slug[lead['slug']]['date']
            newer = [a for a in self.articles if a['date'] > ld and a['slug'] not in placed]
            age = (_dt.date.fromisoformat(self.articles[0]['date']) - _dt.date.fromisoformat(ld)).days
            if newer and age > LEAD_STALE_DAYS:
                out.append(('warn', 'front.json', f'the lead is {age} days older than the newest article and '
                            f'{len(newer)} newer article(s) are unplaced'))
        edition = self.front['edition']
        fresh = [a for a in self.articles if edition and a['date'] > edition]
        if fresh:
            out.append(('todo', 'front.json', f'{len(fresh)} article(s) published since the {edition} edition: '
                        + ', '.join(a['slug'] for a in fresh[:6])))
        for p in self.pitches:
            if p['status'] == 'open':
                out.append(('todo', p['where'], f'open pitch from {p["from"]}: {p["ask"]} for {p["article"]}'))
        for a in self.articles[:12]:
            if not has_graph(a['slug']):
                out.append(('info', f'articles/{a["slug"]}.md', 'no graph yet, so its card has no teaser or topics of its own'))
            if not has_card(a['slug']):
                out.append(('info', f'articles/{a["slug"]}.md', 'no card image yet, so it shows the default card'))
        return out
