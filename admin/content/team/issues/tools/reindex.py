#!/usr/bin/env python3
"""Rebuild issues/index.json from issues/*.md — the board app reads the index when it is served
outside a vault host (no sg.vfs to list the folder). Run after adding or moving a card:
    python3 tools/reindex.py && sgit commit -m "board: ..." && sgit push"""
import json, os, re
base = os.path.join(os.path.dirname(__file__), '..', 'issues')
out = []
for fn in sorted(os.listdir(base)):
    if not fn.endswith('.md'): continue
    t = open(os.path.join(base, fn)).read()
    m = re.match(r'---\n(.*?)\n---\n(.*)', t, re.S)
    if not m: raise SystemExit(f'{fn}: no frontmatter')
    meta = dict(l.split(':', 1) for l in m.group(1).split('\n') if ':' in l)
    meta = {k.strip(): v.strip() for k, v in meta.items()}
    meta['file'] = fn; meta['body'] = m.group(2).strip()
    out.append(meta)
json.dump(out, open(os.path.join(base, 'index.json'), 'w'), indent=1, ensure_ascii=False)
print(f'{len(out)} cards -> issues/index.json')
