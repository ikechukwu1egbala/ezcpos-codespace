#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/pip install -r backend/requirements.txt
cd backend
.venv/bin/python manage.py makemigrations users pos inventory payments expenses sync commerce
.venv/bin/python manage.py migrate
cd "$ROOT/frontend"
flutter create --platforms=android,web,ios . >/dev/null 2>&1 || true
flutter pub get
echo "EZC setup complete."
