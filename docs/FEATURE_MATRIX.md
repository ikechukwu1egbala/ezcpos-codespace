# EZC POS v2 feature coverage

## Included in this archive
- Django/DRF backend foundation and Flutter client foundation
- Authentication, business/branch/user role foundation
- Products, customers, sales, inventory, payments/refunds, expenses, reports
- Offline synchronization foundation with operation IDs
- Suppliers
- Warehouses and per-warehouse stock records
- Stock transfers with draft -> in-transit -> received lifecycle
- Consignment inventory with supplier/customer, received/sold/returned quantities and settlement status
- Multi-currency records and exchange-rate records
- Receipt template and server-generated printable HTML receipt
- Product-image recognition dataset storage and training-job tracking
- Codespaces and GitHub Actions build/test setup

## Still required before commercial production
- Full Flutter UI wiring for every backend module
- Atomic stock transfer/receipt transactions and concurrency locks
- Purchase orders, supplier invoices, supplier payments and landed costs
- Complete currency conversion rules on sales/payments/refunds and historical rate locking
- Full consignment settlement accounting and automatic stock movements
- Real PDF/thermal-printer integrations for Android/iOS
- Real image-recognition model training/export/inference after real product image datasets are collected
- Tenant/branch scoped sync conflict resolution and encrypted offline storage
- PostgreSQL production deployment, Redis/Celery where required, backups, monitoring and alerting
- Subscription billing, device management, agent/referral system and audit/security hardening
- End-to-end integration tests against PostgreSQL and real Android devices
