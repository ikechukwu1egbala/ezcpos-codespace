#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT/backend"
../.venv/bin/python manage.py runserver 0.0.0.0:8000
