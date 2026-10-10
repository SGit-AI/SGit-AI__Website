"""Article versions: every article's published history, read from git, and the diff between versions.

An article is published by adding one file, and corrected by editing it. Readers deserve to know
which version they are reading and what changed, so the history is derived rather than kept by
hand: v1.0.0 is the first commit of the article's file; each later commit that changes the text
(title, summary or body) is the next minor version; a commit that changes only the other front
matter (a LinkedIn link, the site version, a tag) is the next patch. A rename is followed. An
uncommitted edit in the working tree is the next version, "in this release", so the page built for
a release already shows the version the release publishes.

The history is cached in article_versions.json beside this file, so a build in a shallow clone
(which cannot see old commits) still has it. A full clone always recomputes.

Also the diff renderer, shared with article_diff.py: paragraphs aligned with difflib, a word-level
diff inside each changed paragraph, unchanged runs folded to one line.
"""
import difflib, html, json, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'article_versions.json')
TEXT_KEYS = ('title', 'summary')


def _git(root, *a):
    r = subprocess.run(['git', *a], cwd=root, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ''


def split(text):
    """(meta dict, paragraphs). The title and summary lead the paragraphs, so a changed abstract
    shows in a diff like a changed paragraph."""
    fm, body = (text.split('\n---\n', 1) if text.startswith('---') else ('', text))
    meta = {}
    for line in fm.splitlines():
        if ':' in line:
            k, v = line.split(':', 1); meta[k.strip()] = v.strip()
    paras = []
    for block in re.split(r'\n\s*\n', body):
        block = block.strip()
        if not block:
            continue
        # a list is one block in markdown; each item is its own paragraph here, so a changed
        # bullet does not drag the whole list into the diff
        if block.startswith('- '):
            paras += [l.strip() for l in block.split('\n') if l.strip()]
        else:
            paras.append(block)
    head = []
    if meta.get('title'): head.append('# ' + meta['title'])
    if meta.get('summary'): head.append('Summary: ' + meta['summary'])
    return meta, head + paras


def history(root, rel):
    """Committed versions of one article, oldest first: [{version, kind, commit, date, subject, words}]."""
    out = _git(root, 'log', '--follow', '--format=@@%H|%h|%ad|%s', '--date=short', '--name-only', '--', rel)
    commits = []
    for chunk in out.split('@@')[1:]:
        lines = [l for l in chunk.strip().split('\n') if l.strip()]
        full, short, date, subject = lines[0].split('|', 3)
        commits.append((full, short, date, subject, lines[-1] if len(lines) > 1 else rel))
    commits.reverse()
    versions, prev = [], None
    major, minor, patch = 1, 0, 0
    for full, short, date, subject, path in commits:
        text = _git(root, 'show', f'{full}:{path}')
        if not text:
            continue
        if prev is None:
            kind = 'published'
        else:
            pm, pp = split(prev); m, p = split(text)
            if pp != p:
                minor, patch, kind = minor + 1, 0, 'minor'
            elif pm != m:
                patch, kind = patch + 1, 'patch'
            else:
                continue
        versions.append({'version': f'v{major}.{minor}.{patch}', 'kind': kind, 'commit': short, 'full': full,
                         'path': path, 'date': date, 'subject': subject, 'words': len(' '.join(split(text)[1][1:]).split())})
        prev = text
    return versions


def all_histories(root, slugs):
    """{slug: [versions]} for every article, from git when the clone is complete, else the cache."""
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    shallow = _git(root, 'rev-parse', '--is-shallow-repository').strip() != 'false'
    if shallow:
        return {s: cache.get(s, []) for s in slugs}
    hist = {s: history(root, f'admin/content/articles/{s}.md') for s in slugs}
    if hist != {s: cache.get(s) for s in slugs}:
        with open(CACHE, 'w') as f:
            json.dump(hist, f, indent=1, sort_keys=True)
            f.write('\n')
    return hist


def with_working_tree(root, slug, versions, current_text, site_version, today):
    """Append the uncommitted edit, if any, as the version this release publishes."""
    if not versions:
        return [{'version': 'v1.0.0', 'kind': 'published', 'commit': None, 'full': None, 'date': today,
                 'subject': f'site {site_version}, in this release', 'words': len(' '.join(split(current_text)[1][1:]).split()),
                 'pending': True}]
    last = versions[-1]
    old = _git(root, 'show', f'{last["full"]}:{last["path"]}')
    if not old or old == current_text:
        return versions
    pm, pp = split(old); m, p = split(current_text)
    major, minor, patch = (int(x) for x in last['version'][1:].split('.'))
    if pp != p:
        v, kind = f'v{major}.{minor + 1}.0', 'minor'
    elif pm != m:
        v, kind = f'v{major}.{minor}.{patch + 1}', 'patch'
    else:
        return versions
    return versions + [{'version': v, 'kind': kind, 'commit': None, 'full': None, 'date': today,
                        'subject': f'site {site_version}, in this release',
                        'words': len(' '.join(p[1:]).split()), 'pending': True}]


def text_at(root, v, current_text):
    return current_text if v.get('pending') else _git(root, 'show', f'{v["full"]}:{v["path"]}')


# ------------------------------------------------------------------ the diff

def _esc(s):
    return html.escape(s, quote=False)


def _inline(s, up):
    # the escaped text, with the three bits of inline markdown a reader expects rendered:
    # bold, links (as their text, with the target on hover) and inline code
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'<a href="{(up + m.group(2)) if m.group(2).startswith("/") else m.group(2)}">{m.group(1)}</a>' if m.group(2).startswith(('http', '/')) else m.group(1), s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s


def _render_para(p, up, cls=''):
    c = f' class="{cls.strip()}"' if cls else ''
    if p.startswith('!shot'):
        name = p.split('|')[0].replace('!shot', '').strip()
        return f'<p class="diff-fig{cls}">[figure {_esc(name)}] {_esc(p.split("|", 2)[-1].strip())}</p>'
    if p.startswith('## '):
        return f'<h2{c}>{_esc(p[3:])}</h2>'
    if p.startswith('# '):
        return f'<h1>{_esc(p[2:])}</h1>'
    if p.startswith('- '):
        return f'<p class="diff-li{cls}">&bull; {_inline(_esc(p[2:]), up)}</p>'
    return f'<p{c}>{_inline(_esc(p), up)}</p>'


def _word_diff(a, b, up):
    ta, tb = re.findall(r'\s+|[^\s]+', a), re.findall(r'\s+|[^\s]+', b)
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal': out.append(_esc(''.join(ta[i1:i2])))
        if op in ('delete', 'replace'): out.append('<del>' + _esc(''.join(ta[i1:i2])) + '</del>')
        if op in ('insert', 'replace'): out.append('<ins>' + _esc(''.join(tb[j1:j2])) + '</ins>')
    s = _inline(''.join(out), up)
    if b.startswith('## '): return f'<h2 class="changed">{s[3:] if s.startswith("## ") else s}</h2>'
    if b.startswith('- '): return f'<p class="changed diff-li">&bull; {s[2:] if s.startswith("- ") else s}</p>'
    return f'<p class="changed">{s}</p>'


def diff(old_text, new_text, up='../..'):
    """(list of html blocks, stats) for the change from old_text to new_text. `up` is the relative
    path from the page the diff lands on to the site root, for root-relative links."""
    A, B = split(old_text)[1], split(new_text)[1]
    sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
    body = []; st = dict(same=0, added=0, removed=0, changed=0, words_added=0, words_removed=0)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            n = i2 - i1; st['same'] += n
            heads = [p for p in A[i1:i2] if p.startswith('## ')]
            label = f'{n} unchanged paragraph{"s" if n != 1 else ""}'
            if heads: label += ', under ' + ', '.join(_esc(h[3:]) for h in heads[:3]) + ('…' if len(heads) > 3 else '')
            body.append(f'<p class="diff-same">{label}</p>')
        elif op == 'replace' and (i2 - i1) == (j2 - j1):
            for a, b in zip(A[i1:i2], B[j1:j2]):
                body.append(_word_diff(a, b, up)); st['changed'] += 1
                st['words_added'] += max(0, len(b.split()) - len(a.split()))
                st['words_removed'] += max(0, len(a.split()) - len(b.split()))
        else:
            for a in A[i1:i2]:
                body.append(_render_para(a, up, ' removed')); st['removed'] += 1; st['words_removed'] += len(a.split())
            for b in B[j1:j2]:
                body.append(_render_para(b, up, ' added')); st['added'] += 1; st['words_added'] += len(b.split())
    return body, st


DIFF_CSS = ('<style>.diff ins{background:#e6f4ea;color:#1a5c36;text-decoration:none;padding:0 2px}'
            '.diff del{background:#fde8e6;color:#8a1c12;text-decoration:line-through;padding:0 2px}'
            '.diff .diff-same{color:#8a8780;font-size:.85em;border-left:3px solid #e3e0d8;padding-left:.7em;margin:1.2em 0}'
            '.diff .added{border-left:3px solid #1a7f5a;padding-left:.7em}'
            '.diff .removed{border-left:3px solid #b42318;padding-left:.7em;color:#6b6863;text-decoration:line-through}'
            '.diff .changed{border-left:3px solid #b45309;padding-left:.7em}.diff .diff-fig{font-style:italic;color:#6b6863}'
            '.diff .diff-li{margin:.3em 0 .3em 1em}</style>')
