#!/usr/bin/env bash
# Serve the SERIQ site locally with live reload.
#
#   ./serve.sh              # http://localhost:4000
#   ./serve.sh -p 4001      # different port
#   ./serve.sh --build      # one-off build to _site/, no server
#
# Prefers Bundler (reproducible, matches CI). Falls back to a system-wide
# Jekyll when the bundle isn't installed — useful offline.

set -euo pipefail
cd "$(dirname "$0")"

PORT=4000
BUILD_ONLY=0
EXTRA=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    -p|--port)  PORT="$2"; shift 2 ;;
    --build)    BUILD_ONLY=1; shift ;;
    -h|--help)  sed -n '2,10p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *)          EXTRA+=("$1"); shift ;;
  esac
done

if ! command -v jekyll >/dev/null 2>&1 && ! command -v bundle >/dev/null 2>&1; then
  echo "error: neither 'bundle' nor 'jekyll' found." >&2
  echo "Install Ruby, then: gem install bundler && bundle install" >&2
  exit 1
fi

# Use Bundler only if the bundle is actually satisfied; otherwise it aborts
# offline. Falling back keeps the script usable without network access.
RUNNER=(jekyll)
if command -v bundle >/dev/null 2>&1 && bundle check >/dev/null 2>&1; then
  RUNNER=(bundle exec jekyll)
else
  if command -v bundle >/dev/null 2>&1; then
    echo "note: bundle not installed/satisfied — using system Jekyll." >&2
    echo "      run 'bundle install' for a reproducible build." >&2
  fi
  export JEKYLL_NO_BUNDLER_REQUIRE=true
fi

if [[ "$BUILD_ONLY" -eq 1 ]]; then
  exec "${RUNNER[@]}" build --trace "${EXTRA[@]+"${EXTRA[@]}"}"
fi

echo "SERIQ — http://localhost:${PORT}/      (français, défaut)"
echo "        http://localhost:${PORT}/en/   (English)"
echo

exec "${RUNNER[@]}" serve \
  --host 127.0.0.1 \
  --port "$PORT" \
  --livereload \
  --trace \
  "${EXTRA[@]+"${EXTRA[@]}"}"
