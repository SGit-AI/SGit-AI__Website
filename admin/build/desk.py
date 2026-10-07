#!/usr/bin/env python3
"""desk.py — the Editor's checklist, printed. Run it at the start of every desk run.

    python3 admin/build/desk.py            the report
    python3 admin/build/desk.py --json     the same, as JSON, for an agent to parse

It reads exactly what the build reads (admin/content/articles/, the graphs, admin/content/newsroom/)
and writes nothing. The same findings are rendered on /newsroom/ under Desk health.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from content import Content_Loader          # noqa: E402
from newsroom import Newsroom               # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CONTENT = os.path.join(ROOT, 'admin', 'content')


def main():
    L = Content_Loader(CONTENT)
    arts = [a for a in L.load_articles() if a['status'] == 'published']
    graphs = L.load_article_graphs()
    N = Newsroom(L, CONTENT, arts)
    has_card = lambda s: os.path.exists(os.path.join(ROOT, 'articles', 'cards', s + '.webp'))
    rows = N.health(lambda s: s in graphs, has_card)
    fr = N.front
    lead = N.lead()
    since = [a for a in arts if fr['edition'] and a['date'] > fr['edition']]
    unplaced = [a for a in arts[:15] if a['slug'] not in N.placed()]
    report = {
        'edition': fr['edition'], 'lead': lead and lead['slug'],
        'highlights': [h['slug'] for h in fr['highlights']],
        'published_since_edition': [a['slug'] for a in since],
        'recent_unplaced': [a['slug'] for a in unplaced],
        'open_pitches': [p['where'] for p in N.pitches if p['status'] == 'open'],
        'last_run': N.log[0]['where'] if N.log else None,
        'findings': [{'level': l, 'where': w, 'text': t} for l, w, t in rows],
    }
    if '--json' in sys.argv:
        print(json.dumps(report, indent=2))
        return
    print(f'== the desk, edition {fr["edition"] or "(none)"}')
    print(f'   lead:        {report["lead"]}')
    print(f'   highlights:  {", ".join(report["highlights"]) or "(none)"}')
    print(f'   last run:    {report["last_run"] or "(none)"}')
    print(f'\n== published since the edition ({len(since)})')
    for a in since:
        print(f'   {a["date"]}  {a["slug"]}')
    print(f'\n== recent articles that are only in Latest ({len(unplaced)}); a decision, not a fault')
    for a in unplaced:
        print(f'   {a["date"]}  {a["slug"]}')
    print(f'\n== findings ({len(rows)})')
    for l, w, t in sorted(rows, key=lambda r: {'warn': 0, 'todo': 1, 'info': 2}[r[0]]):
        print(f'   [{l}] {w}: {t}')
    print('\nNext: read what is new, answer the pitches, rewrite front.json with a why for every slot, '
          'log the run, build, validate, policy_check.py --role editor, release.')


if __name__ == '__main__':
    main()
