# Production checklist

Before accepting real customer data: use PostgreSQL, HTTPS, strong secret management, tenant isolation tests, backups, monitoring, audit logging, rate limiting, device/session revocation, secure token storage, signed Android/iOS releases, receipt/legal configuration, refund authorization, and disaster recovery.

The API is designed so the Flutter client is not the authority for pricing, stock, totals, payment status or refunds. Those rules belong on the server.

Offline sync uses globally unique `operation_id` values. The server must treat repeated operations as safe retries and must reject cross-tenant operations.
