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

step "5/5 release complete"
# The one file allowed to be dirty afterwards is the vault ref: AES-GCM uses a
# fresh IV per write, so sgit's own push re-encrypts it and git sees a change
# even though it decrypts to the same commit. Anything ELSE dirty is a real
# problem and gets reported.
LEFTOVER="$(git status --porcelain | grep -v '\.sg_vault/bare/refs/' || true)"
[ -z "$LEFTOVER" ] || { echo "note: unexpected dirty files after release:"; echo "$LEFTOVER"; }
echo "both remotes in sync — done."
