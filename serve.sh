#!/usr/bin/env bash
# Serve the SERIQ site locally with live reload.
#
#   ./serve.sh              # http://localhost:4000
#   ./serve.sh -p 4001      # different port
#   ./serve.sh --build      # one-off build to _site/, no server
#
# The LiveReload port is derived from --port, so two servers on different
# ports can run side by side.
#
# Prefers Bundler (reproducible, matches CI). Falls back to a system-wide
# Jekyll when the bundle isn't installed — useful offline.

set -euo pipefail
cd "$(dirname "$0")"

INVOCATION=("$0" "$@")   # kept for the restart hint in check_port

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

# LiveReload's socket is a second port, and Jekyll pins it to 35729 regardless
# of --port — so without this a second server collides with the first even on a
# free --port. 4000 maps to 35729, Jekyll's own default.
LIVERELOAD_PORT=$(( PORT + 31729 ))

# Jekyll reports a busy port as an EventMachine "no acceptor" backtrace that
# names neither the port nor the process, so check first and say it plainly.
listening_pid() {
  command -v ss >/dev/null 2>&1 || return 1
  ss -ltnp "sport = :$1" 2>/dev/null | sed -n 's/.*pid=\([0-9]\+\).*/\1/p' | head -n1
}
port_is_busy() {
  command -v ss >/dev/null 2>&1 || return 1
  [[ -n "$(ss -ltn "sport = :$1" 2>/dev/null | sed -n '2,$p')" ]]
}

check_port() {
  local port="$1" role="$2" pid holder cwd
  port_is_busy "$port" || return 0        # free, or no 'ss' to check with

  pid="$(listening_pid "$port" || true)"
  holder=""
  cwd=""
  if [[ -n "$pid" ]]; then
    holder="$(ps -p "$pid" -o args= 2>/dev/null | cut -c1-72)"
    cwd="$(readlink -f "/proc/$pid/cwd" 2>/dev/null || true)"
  fi

  {
    echo "error: port $port is already in use — $role cannot start."
    if [[ -n "$pid" ]]; then
      echo "       held by pid $pid: ${holder:-(unknown command)}"
    else
      echo "       held by another user's process (no pid visible)."
    fi
    echo
    if [[ -n "$cwd" && "$cwd" == "$PWD" ]]; then
      echo "This is a server for this same site, already running and rebuilding."
      echo "It is serving your current files:"
      echo
      echo "    http://localhost:${PORT}/"
      echo
      echo "Nothing to do — or replace it with:"
      echo
      echo "    kill $pid && ${INVOCATION[*]}"
    else
      echo "Use a different port:"
      echo
      echo "    $0 -p $(( PORT + 1 ))"
      if [[ -n "$pid" ]]; then
        echo
        echo "or stop what is there:"
        echo
        echo "    kill $pid"
      fi
    fi
  } >&2
  exit 1
}

check_port "$PORT" "the web server"
check_port "$LIVERELOAD_PORT" "LiveReload"

echo "SERIQ — http://localhost:${PORT}/      (français, défaut)"
echo "        http://localhost:${PORT}/en/   (English)"
echo

exec "${RUNNER[@]}" serve \
  --host 127.0.0.1 \
  --port "$PORT" \
  --livereload \
  --livereload-port "$LIVERELOAD_PORT" \
  --trace \
  "${EXTRA[@]+"${EXTRA[@]}"}"
