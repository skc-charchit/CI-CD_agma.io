#!/usr/bin/env sh
set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
API_PORT=${API_PORT:-8001}
WEB_PORT=${WEB_PORT:-5501}

cleanup() {
    trap - EXIT INT TERM
    kill "$API_PID" "$WEB_PID" 2>/dev/null || true
    wait "$API_PID" "$WEB_PID" 2>/dev/null || true
}

trap cleanup EXIT INT TERM

cd "$ROOT_DIR"

uv lock --check

PYTHONPATH="$ROOT_DIR/apps/api" uv run --no-sync python -c \
    'import ast, pathlib; [ast.parse(path.read_text()) for path in pathlib.Path("apps/api/app").rglob("*.py")]'

PYTHONPATH="$ROOT_DIR/apps/api" uv run uvicorn app.main:app \
    --host 127.0.0.1 --port "$API_PORT" >/tmp/agma-api-check.log 2>&1 &
API_PID=$!

python3 -m http.server "$WEB_PORT" \
    --bind 127.0.0.1 --directory "$ROOT_DIR/apps/company-web/public" \
    >/tmp/agma-web-check.log 2>&1 &
WEB_PID=$!

uv run --no-sync python tests/smoke_test.py \
    --api-url "http://127.0.0.1:$API_PORT" \
    --web-url "http://127.0.0.1:$WEB_PORT"

git diff --check
printf 'Review checks passed.\n'
