#!/usr/bin/env python3
"""policy_check.py — did this branch write only what the role may write?

    python3 admin/build/policy_check.py --role journalist                  vs origin/dev
    python3 admin/build/policy_check.py --role editor --base HEAD~1
    python3 admin/build/policy_check.py --role contributor --files a b c   check a list instead

The policy is the `writes` and `edits` lists in admin/content/newsroom/roles/<role>.md, the
same files the /newsroom/policies.html table is generated from. Two kinds of path are exempt:

  * build output: every file the build writes (the .html pages, their .md twins, llms files,
    sitemap, feeds, graphs.json). The build writes them for whoever runs it; a role is judged
    on its sources. A path counts as source if it is under admin/ or assets/, or is an image,
    card, dataset or link-preview file.
  * the release lines: SITE_VERSION and the VERSION_LOG rows at the top of build_pages.py,
    which every role that releases must touch. Any other change to build_pages.py is judged.

Exit status 1 if anything is outside the policy, so it can gate a release.
"""
import argparse
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from content import Content_Loader          # noqa: E402
from newsroom import Newsroom               # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SOURCE = re.compile(r'^(admin/|assets/|articles/(images|cards|data)/|og/)')
GENERATED = re.compile(r'^admin/(index|versions)\.(html|md)$|^admin/llms\.txt$|^assets/site-index\.json$')
BUILD = 'admin/build/build_pages.py'


def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout


def release_lines_only(base):
    """True if every hunk of the build_pages.py diff falls in the release block: from the
    SITE_VERSION line to the end of VERSION_LOG (the first line that closes the list)."""
    old = git('show', f'{base}:{BUILD}').split('\n')
    try:
        start = next(i for i, l in enumerate(old) if l.startswith('SITE_VERSION ='))
        vl = next(i for i, l in enumerate(old) if l.startswith('VERSION_LOG = ['))
        end = next(i for i in range(vl, len(old)) if old[i] == ']')
    except StopIteration:
        return False
    for m in re.finditer(r'^@@ -(\d+)(?:,(\d+))?', git('diff', '-U0', base, '--', BUILD), re.M):
        a, n = int(m.group(1)), int(m.group(2) or 1)
        lo, hi = a - 1, a - 1 + max(n, 1)
        if lo < start or hi > end + 1:
            return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--role', required=True)
    ap.add_argument('--base', default='origin/dev')
    ap.add_argument('--files', nargs='*')
    o = ap.parse_args()
    content = os.path.join(ROOT, 'admin', 'content')
    L = Content_Loader(content)
    N = Newsroom(L, content, [a for a in L.load_articles() if a['status'] == 'published'])
    if not N.role(o.role):
        sys.exit(f'no such role {o.role!r}; roles: {", ".join(r["slug"] for r in N.roles)}')
    if o.files is not None:
        files = o.files
    else:
        files = [f for f in git('diff', '--name-only', o.base).split('\n') if f]
        files += [f for f in git('ls-files', '--others', '--exclude-standard').split('\n') if f]
    bad, ok, skipped = [], [], 0
    for f in sorted(set(files)):
        if not SOURCE.match(f) or GENERATED.match(f):
            skipped += 1
            continue
        allowed, why = N.may_write(o.role, f)
        if not allowed and f == BUILD and o.files is None and release_lines_only(o.base):
            allowed, why = True, 'release lines only (SITE_VERSION, VERSION_LOG)'
        (ok if allowed else bad).append((f, why))
    for f, why in ok:
        print(f'  ok    {f}  ({why})')
    for f, why in bad:
        print(f'  OUT   {f}  ({why})')
    print(f'policy {o.role}: {len(ok)} source file(s) inside, {len(bad)} outside, {skipped} build output ignored')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
