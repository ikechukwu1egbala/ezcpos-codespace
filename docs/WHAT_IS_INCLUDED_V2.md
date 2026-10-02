# What this v2 archive covers

The original EZC foundation remains and this version adds a commerce/operations layer for suppliers, warehouses, transfers/in-transit stock, consignments, currencies/exchange rates, receipt templates/HTML receipt rendering, and image-recognition dataset/training-job tracking.

## Receipt generation
The backend endpoint `/api/commerce/receipts/<sale-id>/` returns a print-ready HTML receipt. A production Android thermal-printer/PDF adapter still needs to be selected and integrated; the receipt data/template contract is already separated for that work.

## Image recognition
The backend can collect labeled product images and track training jobs. Actual model training is intentionally not fabricated: a merchant's real images are required. The `recognition_training/README.md` documents the training/export/inference pipeline.

## Currency
Currencies and exchange rates are business-scoped. Sales/payments should store the currency and the applied historical rate at transaction time before production; this is listed as a remaining accounting hardening item.
