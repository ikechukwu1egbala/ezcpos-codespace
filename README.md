# EZC POS — Codespace Edition

A production-oriented Nigerian retail/wholesale POS foundation built around **Flutter + Django REST Framework + PostgreSQL** with an offline-first sync design.

## What is included
- Flutter mobile POS UI for login, dashboard, products, sales, customers, expenses and settings.
- Django REST API with JWT authentication.
- Tenant/business and branch-aware data model.
- Products, customers, sales, payments, expenses and inventory movements.
- Idempotent sync operation endpoint using `operation_id`.
- SQLite for zero-setup development; PostgreSQL-ready configuration for deployment.
- Automated Python tests and GitHub Actions for Flutter analyze/test/build and backend tests.
- Codespaces configuration with Flutter 3.47.0 stable.

## Important
This archive is the **complete runnable project foundation**, not a claim that a production SaaS can be safely deployed without configuring secrets, PostgreSQL, HTTPS, backups, monitoring, payments and final acceptance testing. Those production controls are documented in `docs/PRODUCTION.md`.

## Run in GitHub Codespaces
```bash
cd /workspaces/Ezcpos
# If this archive was extracted elsewhere, cd to its root instead.
./scripts/setup.sh
./scripts/test.sh
./scripts/run_backend.sh
```

In a second terminal:
```bash
cd frontend
flutter pub get
flutter analyze
flutter test
flutter run -d chrome
```

For Android APK in Codespaces/CI:
```bash
cd frontend
flutter build apk --release
```

See `docs/CODESPACES.md` for the exact first-time procedure.
