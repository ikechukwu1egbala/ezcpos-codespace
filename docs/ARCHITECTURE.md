# EZC architecture

Flutter owns presentation, local state and the offline outbox. Django owns authentication, tenant authorization, pricing, stock, sales totals, payments, refunds and reporting. PostgreSQL is the production source of truth.

Sync operations are identified by UUID `operation_id`; retries must be idempotent. Every server-side query is scoped through the authenticated user's business.
