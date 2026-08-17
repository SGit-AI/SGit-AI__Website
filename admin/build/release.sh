#!/usr/bin/env bash
# release.sh — the one way this site ships.
#
#   ./admin/build/release.sh "site v0.2.2: what changed"
#
# One working tree, two remotes (see /case-studies/one-tree-two-remotes.html):
# the sgit push carries the encrypted history other sessions clone; the git push
# is the public mirror and triggers the GitHub Pages deploy. A release is not
# done until BOTH remotes report in sync, and nothing is pushed anywhere until
# the validator — including the vault-key leak tripwire — has passed.
#
# This script never prints the vault key. Do not add calls to commands that
# echo it (e.g. `sgit vault info`, `sgit vault show-key`): release logs get
# pasted into issues, chats and CI output, which is exactly how keys leak.
set -euo pipefail

MSG="${1:?usage: release.sh \"commit message\"}"
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

step() { printf '\n\033[1m== %s\033[0m\n' "$*"; }
die()  { printf '\033[31mRELEASE ABORTED: %s\033[0m\n' "$*" >&2; exit 1; }

[ -f app.json ] || die "not at the vault root (no app.json)"
[ -d .git ] && [ -d .sg_vault ] || die "expected both .git and .sg_vault here"

step "1/5 build"
python3 admin/build/build_pages.py || die "build failed"

step "2/5 validate (includes the key-leak tripwire)"
# validate.js reads the passphrase from the gitignored .sg_vault/local/ tier at
# runtime and scans every tracked file for it — a key in the tree fails here,
# before either remote can be touched.
node admin/build/validate.js || die "validation failed — nothing was pushed"

step "3/5 sgit: commit + push the vault"
sgit commit -m "$MSG" >/dev/null || true          # "nothing to commit" is fine
sgit push || die "sgit push failed"
sgit status 2>&1 | grep -q "in sync with remote" \
  || die "sgit reports the vault is NOT in sync after push"
echo "   vault: in sync with remote"

step "4/5 git: commit + push the mirror"
git add -A
git diff --cached --quiet || git commit -q -m "$MSG"
BRANCH="$(git branch --show-current)"
n=0
until git push -u origin "$BRANCH"; do
  n=$((n+1)); [ $n -ge 4 ] && die "git push failed after 4 attempts"
  sleep $((2**n))
done
[ "$(git rev-parse HEAD)" = "$(git rev-parse "origin/$BRANCH")" ] \
  || die "git HEAD != origin/$BRANCH after push"
echo "   git: HEAD == origin/$BRANCH"

step "5/6 verify the deploy actually published"
# "Both remotes in sync" is NOT the same as "live", and on 17 August that gap cost
# two releases. v0.2.31 and v0.2.32 both pushed cleanly and both reported success
# here, while GitHub Pages failed to deploy either one: codeload returned 429 (Too
# Many Requests) for actions/configure-pages@v5 and the deploy job died in "Set up
# job", before running a step. The site served a two-release-old page for forty
# minutes and nothing noticed — the failure was in a job neither remote knows about.
#
# So the last thing a release does is ask the live site what version it is serving.
# The cost is up to eight minutes of waiting; the alternative is telling somebody a
# fix is live when it is not, which happened twice in one afternoon.
VER="$(sed -n "s/^SITE_VERSION = '\(.*\)'\$/\1/p" admin/build/build_pages.py)"
[ -n "$VER" ] || die "could not read SITE_VERSION from admin/build/build_pages.py"
echo "   waiting for $VER to appear at https://sgit.ai/ (up to 8 min)"
LIVE=""
for i in $(seq 1 32); do
  sleep 15
  # cache-buster: GitHub Pages serves max-age=600, and we want the origin's answer
  LIVE="$(curl -sS "https://sgit.ai/index.html?deploycheck=$i" 2>/dev/null \
          | grep -o 'v0\.[0-9]\+\.[0-9]\+' | head -1 || true)"
  [ "$LIVE" = "$VER" ] && break
  printf '.'
done
echo
if [ "$LIVE" = "$VER" ]; then
  echo "   live: sgit.ai is serving $VER"
else
  echo "   live: sgit.ai is still serving ${LIVE:-<unknown>}, expected $VER" >&2
  echo "   the push succeeded — this is the GitHub Pages deploy, not the content." >&2
  echo "   check:  https://github.com/SGit-AI/SGit-AI__Website/actions" >&2
  echo "   a 429 downloading actions/configure-pages is transient; re-run the job." >&2
  die "pushed but NOT published — do not report this release as live"
fi

step "6/6 release complete"
# Because sgit pushed before git committed, the tree should end clean — the git
# mirror includes the exact ref that push wrote. A dirty ref here means the
# ordering was violated somewhere; it is tolerated (a rewritten ref can decrypt
# to the same commit — fresh AES-GCM IV per write) but anything else dirty is a
# real problem and gets reported.
LEFTOVER="$(git status --porcelain | grep -v '\.sg_vault/bare/refs/' || true)"
[ -z "$LEFTOVER" ] || { echo "note: unexpected dirty files after release:"; echo "$LEFTOVER"; }
echo "both remotes in sync — done."
