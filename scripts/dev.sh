#!/usr/bin/env sh
set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
API_PORT=${API_PORT:-8000}
WEB_PORT=${WEB_PORT:-5500}

cleanup() {
    trap - EXIT INT TERM
    kill "$API_PID" "$WEB_PID" 2>/dev/null || true
    wait "$API_PID" "$WEB_PID" 2>/dev/null || true
}

trap cleanup EXIT INT TERM

cd "$ROOT_DIR"

PYTHONPATH="$ROOT_DIR/apps/api" uv run uvicorn app.main:app \
    --reload --host 127.0.0.1 --port "$API_PORT" &
API_PID=$!

python3 -m http.server "$WEB_PORT" \
    --bind 127.0.0.1 --directory "$ROOT_DIR/apps/company-web/public" &
WEB_PID=$!

printf 'Company web: http://127.0.0.1:%s\n' "$WEB_PORT"
printf 'Platform API: http://127.0.0.1:%s/docs\n' "$API_PORT"
printf 'Press Ctrl+C to stop both services.\n'

wait "$API_PID" "$WEB_PID"
