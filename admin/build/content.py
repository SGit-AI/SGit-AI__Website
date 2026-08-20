"""content.py — markdown content types: Updates and Articles.

Adopted from the VoiceDebrief journalist pipeline (CC BY 4.0, same house), whose
central rule is the one worth copying verbatim:

    PUBLISHING IS ADDING ONE FILE. NOTHING ELSE.

No index to update, no HTML to splice, no manifest to hand-edit, no decision about
where a post goes. Ordering, ids, markup, the JSON manifest and the RSS feed are all
derived at build time. Two agents publishing on the same day touch two different files
and cannot conflict — which is the property that makes an unattended journalist agent
safe to run at all.

Layout:
    admin/content/updates/YYYY/MM/DD/<version>__update__<slug>.md
    admin/content/articles/<slug>.md

ONE DELIBERATE DIVERGENCE from the VoiceDebrief contract. There, internal links are
root-relative (`/updates/`) because the site is served from a domain root. This site
must also render from INSIDE A VAULT, where the app is mounted at an arbitrary path and
a leading slash escapes it. So posts are still authored with root-relative links — one
form, no counting of `../` by hand — and the build rewrites each to a depth-relative
path for the page it lands on. Authors get the simple rule; the vault still works.
"""
import html
import json
import os
import re

LIST_KEYS = {'tags'}


class Content_Error(Exception):
    pass


class Content_Loader:
    """Loads, validates and renders the markdown content types."""

    def __init__(self, content_root):
        self.root = content_root

    # ---------------------------------------------------------------- frontmatter

    def parse_frontmatter(self, text, where):
        """Flat `key: value` between --- fences. No YAML dependency, nothing nested
        to get subtly wrong, and a malformed line names itself."""
        if not text.startswith('---'):
            raise Content_Error(f'{where}: must start with a --- frontmatter block')
        end = text.find('\n---', 3)
        if end < 0:
            raise Content_Error(f'{where}: frontmatter is not closed with ---')
        meta, body = {}, text[end + 4:].lstrip('\n')
        for i, line in enumerate(text[3:end].strip().split('\n'), 1):
            if not line.strip():
                continue
            if ':' not in line:
                raise Content_Error(f'{where}: frontmatter line {i} is not `key: value` — {line!r}')
            k, v = line.split(':', 1)
            k, v = k.strip(), v.strip()
            meta[k] = [x.strip() for x in v.split(',') if x.strip()] if k in LIST_KEYS else v
        return meta, body

    # ---------------------------------------------------------------- markdown

    def _link_href(self, href, depth, where):
        if re.match(r'^(https?://|#|mailto:)', href):
            return href
        if href.startswith('/'):
            # root-relative in source, depth-relative in output — see the module note
            return '../' * depth + href.lstrip('/')
        raise Content_Error(
            f'{where}: link target must be root-relative, absolute or an anchor — got {href!r}')

    def inline(self, s, depth, where):
        """Escape first, then the small inline set. The content is ours; a page is
        still never built by trusting a string."""
        s = html.escape(s, quote=False)
        s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
        s = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', s)
        s = re.sub(r'(?<![*\w])\*([^*\n]+)\*', r'<em>\1</em>', s)

        def link(m):
            text, href = m.group(1), self._link_href(m.group(2), depth, where)
            return f'<a href="{html.escape(href, quote=True)}">{text}</a>'

        return re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', link, s)

    def md_to_html(self, md, depth=0, where=''):
        """Headings, paragraphs, bullet and numbered lists, quotes, fenced code,
        rules — plus one site-specific block, the `!shot` figure, which emits the
        walkthrough figure the screenshot component fills at runtime."""
        out, para, lst, fence = [], [], None, None

        def flush_para():
            if para:
                out.append('<p>' + self.inline(' '.join(para), depth, where) + '</p>')
                para.clear()

        def flush_list():
            nonlocal lst
            if lst:
                out.append(f'</{lst}>')
                lst = None

        lines = md.split('\n')
        i = -1
        while i + 1 < len(lines):
            i += 1
            raw = lines[i]
            line = raw.rstrip()

            if fence is not None:
                if line.strip().startswith('```'):
                    out.append('</pre>')
                    fence = None
                else:
                    out.append(html.escape(line, quote=False))
                continue
            if line.strip().startswith('```'):
                flush_para(); flush_list()
                out.append('<pre class="shell">')
                fence = True
                continue

            if not line.strip():
                flush_para(); flush_list()
                continue

            # !shot filename.webp | dir | caption   — a walkthrough figure
            if line.startswith('!shot '):
                flush_para(); flush_list()
                parts = [p.strip() for p in line[6:].split('|')]
                name = parts[0]
                sdir = parts[1] if len(parts) > 1 and parts[1] else 'images/'
                cap = parts[2] if len(parts) > 2 else ''
                out.append(
                    f'<figure class="shot" data-shot="{html.escape(name, quote=True)}" '
                    f'data-dir="{html.escape(sdir, quote=True)}" '
                    f'data-alt="{html.escape(cap, quote=True)}">'
                    f'<figcaption>{self.inline(cap, depth, where)}</figcaption></figure>')
                continue

            if line.startswith('|') and i + 1 < len(lines) \
                    and re.match(r'^\|[\s:|-]+\|$', lines[i + 1].strip()):
                flush_para(); flush_list()

                def cells(row):
                    return [c.strip() for c in row.strip().strip('|').split('|')]

                head = cells(line)
                out.append('<div class="tablewrap"><table>')
                out.append('<tr>' + ''.join(
                    f'<th>{self.inline(c, depth, where)}</th>' for c in head) + '</tr>')
                i += 1                                    # consume the separator
                while i + 1 < len(lines) and lines[i + 1].strip().startswith('|'):
                    i += 1
                    out.append('<tr>' + ''.join(
                        f'<td>{self.inline(c, depth, where)}</td>' for c in cells(lines[i])) + '</tr>')
                out.append('</table></div>')
                continue

            m = re.match(r'^(#{2,4})\s+(.*)$', line)
            if m:
                flush_para(); flush_list()
                lvl = len(m.group(1))
                out.append(f'<h{lvl}>' + self.inline(m.group(2), depth, where) + f'</h{lvl}>')
                continue

            if line.strip() == '---':
                flush_para(); flush_list()
                out.append('<hr>')
                continue

            if line.startswith('> '):
                flush_para(); flush_list()
                out.append('<div class="note">' + self.inline(line[2:], depth, where) + '</div>')
                continue

            m = re.match(r'^[-*]\s+(.*)$', line)
            if m:
                flush_para()
                if lst != 'ul':
                    flush_list(); out.append('<ul>'); lst = 'ul'
                out.append('<li>' + self.inline(m.group(1), depth, where) + '</li>')
                continue

            m = re.match(r'^\d+\.\s+(.*)$', line)
            if m:
                flush_para()
                if lst != 'ol':
                    flush_list(); out.append('<ol>'); lst = 'ol'
                out.append('<li>' + self.inline(m.group(1), depth, where) + '</li>')
                continue

            flush_list()
            para.append(line.strip())

        flush_para(); flush_list()
        if fence is not None:
            raise Content_Error(f'{where}: unclosed ``` fence')
        return '\n'.join(out)

    def md_to_text(self, md, limit=260):
        """Plain-text summary for the manifest and the feed."""
        t = re.sub(r'!shot .*', '', md)
        t = re.sub(r'```.*?```', '', t, flags=re.S)
        t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
        t = re.sub(r'[#>*`_-]', ' ', t)
        t = ' '.join(t.split())
        return t[:limit].rstrip() + ('…' if len(t) > limit else '')

    # ---------------------------------------------------------------- loaders

    RE_DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')

    def _require(self, meta, keys, where):
        for k in keys:
            if not meta.get(k):
                raise Content_Error(f'{where}: frontmatter is missing `{k}:`')

    def load_updates(self):
        """admin/content/updates/YYYY/MM/DD/<version>__update__<slug>.md"""
        base = os.path.join(self.root, 'updates')
        posts = []
        if not os.path.isdir(base):
            return posts
        for dirpath, _dirs, files in os.walk(base):
            for fn in sorted(files):
                if not fn.endswith('.md'):
                    continue
                path = os.path.join(dirpath, fn)
                where = os.path.relpath(path, self.root)
                meta, body = self.parse_frontmatter(open(path).read(), where)
                self._require(meta, ['title', 'date'], where)
                if not self.RE_DATE.match(meta['date']):
                    raise Content_Error(f'{where}: date must be YYYY-MM-DD, got {meta["date"]!r}')
                # the folder is the date — a mismatch means one of them is a typo, and
                # sorting the feed by a date the path disagrees with is how a post
                # silently lands in the wrong place
                folder_date = '-'.join(os.path.relpath(dirpath, base).split(os.sep))
                if folder_date != meta['date']:
                    raise Content_Error(
                        f'{where}: folder says {folder_date}, frontmatter says {meta["date"]}')
                slug = fn[:-3].split('__update__')[-1]
                posts.append({
                    'slug': slug, 'title': meta['title'], 'date': meta['date'],
                    'version': meta.get('version', ''), 'tags': meta.get('tags', []),
                    'status': meta.get('status', 'published'),
                    'summary': self.md_to_text(body), 'body': body, 'where': where,
                })
        posts.sort(key=lambda p: (p['date'], p['slug']), reverse=True)
        seen = set()
        for p in posts:
            if p['slug'] in seen:
                raise Content_Error(f'{p["where"]}: duplicate slug {p["slug"]!r} — permalinks must be unique')
            seen.add(p['slug'])
        return posts

    def load_articles(self):
        """admin/content/articles/<slug>.md — one page each."""
        base = os.path.join(self.root, 'articles')
        arts = []
        if not os.path.isdir(base):
            return arts
        for fn in sorted(os.listdir(base)):
            if not fn.endswith('.md'):
                continue
            where = f'articles/{fn}'
            meta, body = self.parse_frontmatter(open(os.path.join(base, fn)).read(), where)
            self._require(meta, ['title', 'date', 'summary'], where)
            if not self.RE_DATE.match(meta['date']):
                raise Content_Error(f'{where}: date must be YYYY-MM-DD, got {meta["date"]!r}')
            arts.append({
                'slug': fn[:-3], 'title': meta['title'], 'date': meta['date'],
                'summary': meta['summary'], 'tags': meta.get('tags', []),
                'version': meta.get('version', ''),
                'status': meta.get('status', 'published'),
                'body': body, 'where': where,
            })
        arts.sort(key=lambda a: a['date'], reverse=True)
        return arts

    def load_sites(self):
        """admin/content/sites/<slug>.md — one sibling site per file.

        There will be many of these. Adding one is writing this file and capturing
        its screenshots; the index, the cards and the page are all derived."""
        base = os.path.join(self.root, 'sites')
        sites = []
        if not os.path.isdir(base):
            return sites
        for fn in sorted(os.listdir(base)):
            if not fn.endswith('.md'):
                continue
            where = f'sites/{fn}'
            meta, body = self.parse_frontmatter(open(os.path.join(base, fn)).read(), where)
            self._require(meta, ['title', 'domain', 'tagline', 'summary', 'observed'], where)
            if not self.RE_DATE.match(meta['observed']):
                raise Content_Error(f'{where}: observed must be YYYY-MM-DD')
            sites.append({
                'slug': fn[:-3], 'title': meta['title'], 'domain': meta['domain'],
                'tagline': meta['tagline'], 'summary': meta['summary'],
                'observed': meta['observed'], 'repo': meta.get('repo', ''),
                'seen_version': meta.get('seen_version', ''),
                'hero': meta.get('hero', ''), 'tags': meta.get('tags', []),
                'status': meta.get('status', 'published'),
                'body': body, 'where': where,
            })
        sites.sort(key=lambda x: x['domain'])
        return sites

    # ---------------------------------------------------------------- feed

    def render_feed(self, posts, site='https://sgit.ai'):
        def esc(s):
            return html.escape(s, quote=True)
        items = []
        for p in posts[:20]:
            link = f'{site}/updates/index.html#{p["slug"]}'
            items.append(
                '    <item>\n'
                f'      <title>{esc(p["title"])}</title>\n'
                f'      <link>{link}</link>\n'
                f'      <guid isPermaLink="true">{link}</guid>\n'
                f'      <pubDate>{p["date"]}</pubDate>\n'
                f'      <description>{esc(p["summary"])}</description>\n'
                '    </item>')
        return ('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<rss version="2.0">\n  <channel>\n'
                '    <title>sgit.ai — updates</title>\n'
                f'    <link>{site}/updates/index.html</link>\n'
                '    <description>What changed on sgit and on this site, as it happens.</description>\n'
                + '\n'.join(items) + '\n  </channel>\n</rss>\n')
