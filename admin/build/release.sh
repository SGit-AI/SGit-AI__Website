#!/usr/bin/env bash
# release.sh — the one way this site ships.
#
#   ./admin/build/release.sh "site v0.2.2: what changed"
#
# The site ships over git: a push to dev triggers the GitHub Pages deploy. Nothing is
# pushed until the validator — including the vault-key leak tripwire — has passed, and
# a release is not done until https://sgit.ai/ is actually serving the new version.
#
# Until v0.2.76 this folder was also an sgit vault and every release pushed it too
# (see /case-studies/one-tree-two-remotes.html). That mirror was retired and purged at
# v0.2.84; the only vault this script touches now is the board, which it PULLS (step 0).
#
# This script never prints a vault key. Do not add calls to commands that echo one
# (e.g. `sgit vault info`, `sgit vault show-key`): release logs get pasted into issues,
# chats and CI output, which is exactly how keys leak.
set -euo pipefail

MSG="${1:?usage: release.sh \"commit message\"}"
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

step() { printf '\n\033[1m== %s\033[0m\n' "$*"; }
die()  { printf '\033[31mRELEASE ABORTED: %s\033[0m\n' "$*" >&2; exit 1; }

[ -f app.json ] || die "not at the site root (no app.json)"
[ -d .git ] || die "expected a .git here"
[ ! -e .sg_vault ] || die ".sg_vault is present at the site root — the mirror was retired; remove it (it is gitignored, but it should not be here)"

step "0/5 pull the board vault"
# The board is a separate vault (source of truth for team/board.html), cloned under
# admin/content/team/issues/. Pull it so the snapshot this release renders is current.
if [ -d admin/content/team/issues/.sg_vault ]; then
  (cd admin/content/team/issues && sgit pull >/dev/null 2>&1) && echo "   board vault: pulled" \
    || echo "   board vault: pull failed — rendering the last local copy" >&2
else
  echo "   board vault: not cloned here — rendering the tracked cards as they are"
fi

step "1/5 build"
# Link-preview cards first, because the build refuses if an article has a hero figure
# and no card. Needs sharp, which lives with the capture harness, so it is skipped
# where that is not installed and the build then tells you what to run.
if node -e "require.resolve('sharp')" >/dev/null 2>&1; then
  node admin/build/make_og_cards.mjs || die "link-preview cards failed"
else
  echo "   link-preview cards: sharp not installed here, skipping the regeneration"
fi
python3 admin/build/build_pages.py || die "build failed"

step "2/5 validate (includes the key-leak tripwire)"
# validate.js reads every demo vault's write key from the gitignored admin/local/demo-keys/
# folder at runtime and scans every tracked file for each — a key in the tree fails here,
# before anything is pushed.
node admin/build/validate.js || die "validation failed — nothing was pushed"

step "3/5 git: commit + push"
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
echo "   git: HEAD == origin/$BRANCH ($(git rev-parse --short HEAD))"

step "4/5 verify the deploy actually published"
# A clean push is NOT the same as "live", and on 17 August that gap cost two releases.
# v0.2.31 and v0.2.32 both pushed cleanly and both reported success here, while GitHub
# Pages failed to deploy either one: codeload returned 429 (Too Many Requests) for
# actions/configure-pages@v5 and the deploy job died in "Set up job", before running a
# step. The site served a two-release-old page for forty minutes and nothing noticed.
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

step "5/5 release complete"
LEFTOVER="$(git status --porcelain || true)"
[ -z "$LEFTOVER" ] || { echo "note: unexpected dirty files after release:"; echo "$LEFTOVER"; }
echo "release complete — $VER is live."
