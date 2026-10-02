#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
.venv/bin/python backend/manage.py check
.venv/bin/python backend/manage.py test
cd frontend
flutter analyze
flutter test
echo "All configured tests passed."
