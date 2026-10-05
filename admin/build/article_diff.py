#!/usr/bin/env python3
"""Render the changes to an article between two revisions as a page a person can read.

    python3 admin/build/article_diff.py <slug> [rev_a] [rev_b]

rev_a defaults to the last commit that touched the article before HEAD's version
(so "the previous published version"), rev_b to the working tree. The page is written
as a body fragment to admin/content/articles/diffs/<slug>.html and registered in
pages.json, so the normal build gives it the site chrome and a markdown twin. Paragraphs
are aligned with difflib; changed paragraphs get a word-level diff, with insertions in
<ins> and deletions in <del>; runs of unchanged paragraphs are folded to one line so the
reader sees only what moved. Built in the session of 5 October 2026 because reading a
revised 9,000-word article for the changes was slower than building the tool.
"""
import sys, os, re, json, subprocess, difflib, html

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
slug = sys.argv[1]
md_path = f'admin/content/articles/{slug}.md'

def git(*a):
    return subprocess.run(['git', *a], cwd=ROOT, capture_output=True, text=True).stdout

rev_a = sys.argv[2] if len(sys.argv) > 2 else None
rev_b = sys.argv[3] if len(sys.argv) > 3 else None
if rev_a is None:
    rev_a = git('log', '-1', '--format=%h', '--', md_path).strip()
old = git('show', f'{rev_a}:{md_path}')
new = git('show', f'{rev_b}:{md_path}') if rev_b else open(os.path.join(ROOT, md_path)).read()
label_a = git('log', '-1', '--format=%h, %ad, %s', '--date=short', rev_a).strip()
label_b = (git('log', '-1', '--format=%h, %ad, %s', '--date=short', rev_b).strip() if rev_b else 'the working tree, the version being built now')

def split(text):
    fm, body = (text.split('\n---\n', 1) if text.startswith('---') else ('', text))
    meta = {}
    for line in fm.splitlines():
        if ':' in line:
            k, v = line.split(':', 1); meta[k.strip()] = v.strip()
    paras = []
    for block in re.split(r'\n\s*\n', body):
        block = block.strip()
        if not block: continue
        # a list is one block in markdown; each item is its own paragraph here, so a changed
        # bullet does not drag the whole list into the diff
        if block.startswith('- '):
            paras += [l.strip() for l in block.split('\n') if l.strip()]
        else:
            paras.append(block)
    head = []
    if meta.get('title'): head.append('# ' + meta['title'])
    if meta.get('summary'): head.append('Summary: ' + meta['summary'])
    return head + paras, meta

A, meta_a = split(old)
B, meta_b = split(new)

def tokens(p):
    return re.findall(r'\s+|[^\s]+', p)

def esc(s):
    return html.escape(s, quote=False)

def inline(s):
    # the escaped text, with the three bits of inline markdown a reader expects rendered:
    # bold, links (as their text, with the target on hover) and inline code
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'<a href="{("../.." + m.group(2)) if m.group(2).startswith("/") else m.group(2)}">{m.group(1)}</a>' if m.group(2).startswith(('http', '/')) else m.group(1), s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s

def render_para(p, cls=''):
    if p.startswith('!shot'):
        name = p.split('|')[0].replace('!shot', '').strip()
        return f'<p class="diff-fig{cls}">[figure {esc(name)}] {esc(p.split("|", 2)[-1].strip())}</p>'
    if p.startswith('## '):
        return f'<h2{cls and " class=" + chr(34) + cls.strip() + chr(34)}>{esc(p[3:])}</h2>'
    if p.startswith('# '):
        return f'<h1>{esc(p[2:])}</h1>'
    if p.startswith('- '):
        return f'<p class="diff-li{cls}">&bull; {inline(esc(p[2:]))}</p>'
    return f'<p{cls and " class=" + chr(34) + cls.strip() + chr(34)}>{inline(esc(p))}</p>'

def word_diff(a, b):
    ta, tb = tokens(a), tokens(b)
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal': out.append(esc(''.join(ta[i1:i2])))
        if op in ('delete', 'replace'): out.append('<del>' + esc(''.join(ta[i1:i2])) + '</del>')
        if op in ('insert', 'replace'): out.append('<ins>' + esc(''.join(tb[j1:j2])) + '</ins>')
    s = inline(''.join(out))
    if b.startswith('## '): return f'<h2 class="changed">{s[3:] if s.startswith("## ") else s}</h2>'
    if b.startswith('- '): return f'<p class="changed diff-li">&bull; {s[2:] if s.startswith("- ") else s}</p>'
    return f'<p class="changed">{s}</p>'

sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
body = []; n_same = n_ins = n_del = n_chg = 0; w_ins = w_del = 0
def wc(ps): return sum(len(p.split()) for p in ps)
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'equal':
        n = i2 - i1; n_same += n
        heads = [p for p in A[i1:i2] if p.startswith('## ')]
        label = f'{n} unchanged paragraph{"s" if n != 1 else ""}'
        if heads: label += ', under ' + ', '.join(esc(h[3:]) for h in heads[:3]) + ('…' if len(heads) > 3 else '')
        body.append(f'<p class="diff-same">{label}</p>')
    elif op == 'replace' and (i2 - i1) == (j2 - j1):
        for a, b in zip(A[i1:i2], B[j1:j2]):
            body.append(word_diff(a, b)); n_chg += 1
            w_ins += max(0, len(b.split()) - len(a.split())); w_del += max(0, len(a.split()) - len(b.split()))
    else:
        for a in A[i1:i2]: body.append(render_para(a, ' removed')); n_del += 1; w_del += len(a.split())
        for b in B[j1:j2]: body.append(render_para(b, ' added')); n_ins += 1; w_ins += len(b.split())

title_now = meta_b.get('title', slug)
out = [f'<main class="doc diff">',
       f' <p class="crumb"><a href="../../index.html">Home</a> / <a href="../index.html">Articles</a> / <a href="../{slug}.html">{esc(title_now.split(":")[0])}</a> / Changes</p>',
       f' <h1>What changed in: {esc(title_now.split(":")[0])}</h1>',
       f' <p class="lead">The article <a href="../{slug}.html">{esc(title_now)}</a>, compared paragraph by paragraph between two versions. '
       f'From: {esc(label_a)}. To: {esc(label_b)}.</p>',
       f' <p class="small dim">{n_ins} paragraph{"s" if n_ins != 1 else ""} added, {n_del} removed, {n_chg} changed in place, {n_same} unchanged. '
       f'About {w_ins:,} words added and {w_del:,} removed. Insertions are marked like <ins>this</ins>, deletions like <del>this</del>; '
       f'unchanged runs are folded to one line. Figures appear as their file names. Generated by admin/build/article_diff.py from the git history.</p>',
       ' <style>.diff ins{background:#e6f4ea;color:#1a5c36;text-decoration:none;padding:0 2px}.diff del{background:#fde8e6;color:#8a1c12;text-decoration:line-through;padding:0 2px}'
       '.diff .diff-same{color:#8a8780;font-size:.85em;border-left:3px solid #e3e0d8;padding-left:.7em;margin:1.2em 0}.diff .added{border-left:3px solid #1a7f5a;padding-left:.7em}'
       '.diff .removed{border-left:3px solid #b42318;padding-left:.7em;color:#6b6863;text-decoration:line-through}.diff .changed{border-left:3px solid #b45309;padding-left:.7em}.diff .diff-fig{font-style:italic;color:#6b6863}.diff .diff-li{margin:.3em 0 .3em 1em}</style>']
out += [' ' + b for b in body]
out.append(f' <p class="small dim" style="margin-top:2rem"><a href="../{slug}.html">&larr; Back to the article</a></p>')
out.append('</main>')
os.makedirs(os.path.join(ROOT, 'admin/content/articles/diffs'), exist_ok=True)
frag = f'admin/content/articles/diffs/{slug}.html'
open(os.path.join(ROOT, frag), 'w').write('\n'.join(out) + '\n')

pj = os.path.join(ROOT, 'admin/content/pages.json')
pages = json.load(open(pj))
path = f'articles/diffs/{slug}.html'
entry = {'path': path, 'section': 'articles', 'title': f'What changed in: {title_now.split(":")[0]}, sgit.ai',
         'desc': f'The changes to the article "{title_now.split(":")[0]}" between two published versions, paragraph by paragraph, with insertions and deletions marked.'}
if not any(p.get('path') == path for p in pages):
    pages.append(entry); json.dump(pages, open(pj, 'w'), indent=2, ensure_ascii=False); open(pj, 'a').write('\n')
print(f'wrote {frag}: +{n_ins} -{n_del} ~{n_chg} ={n_same} paragraphs; +{w_ins} -{w_del} words; from {rev_a} to {rev_b or "working tree"}')
