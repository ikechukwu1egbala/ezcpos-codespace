from decimal import Decimal
from django.conf import settings
from django.db import models

class Supplier(models.Model):
    business = models.ForeignKey("users.Business", on_delete=models.CASCADE, related_name="suppliers")
    name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=160, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["name"]
    def __str__(self): return self.name

class Warehouse(models.Model):
    business = models.ForeignKey("users.Business", on_delete=models.CASCADE, related_name="warehouses")
    name = models.CharField(max_length=160)
    code = models.CharField(max_length=50)
    address = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)
    class Meta:
        constraints = [models.UniqueConstraint(fields=["business", "code"], name="unique_warehouse_code_per_business")]
    def __str__(self): return self.name

class WarehouseStock(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="stocks")
    product = models.ForeignKey("pos.Product", on_delete=models.CASCADE, related_name="warehouse_stocks")
    quantity = models.DecimalField(max_digits=16, decimal_places=3, default=0)
    reserved_quantity = models.DecimalField(max_digits=16, decimal_places=3, default=0)
    class Meta:
        constraints = [models.UniqueConstraint(fields=["warehouse", "product"], name="unique_product_per_warehouse")]

class StockTransfer(models.Model):
    STATUS = [("draft","Draft"),("in_transit","In transit"),("received","Received"),("cancelled","Cancelled")]
    business = models.ForeignKey("users.Business", on_delete=models.CASCADE, related_name="stock_transfers")
    reference = models.CharField(max_length=80, unique=True)
    source = models.ForeignKey(Warehouse, on_delete=models.PROTECT, related_name="outgoing_transfers")
    destination = models.ForeignKey(Warehouse, on_delete=models.PROTECT, related_name="incoming_transfers")
    status = models.CharField(max_length=20, choices=STATUS, default="draft")
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    shipped_at = models.DateTimeField(null=True, blank=True)
    received_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class StockTransferItem(models.Model):
    transfer = models.ForeignKey(StockTransfer, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("pos.Product", on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=16, decimal_places=3)

class Consignment(models.Model):
    STATUS = [("open","Open"),("partially_settled","Partially settled"),("settled","Settled"),("returned","Returned")]
    business = models.ForeignKey("users.Business", on_delete=models.CASCADE, related_name="consignments")
    supplier = models.ForeignKey(Supplier, null=True, blank=True, on_delete=models.SET_NULL, related_name="consignments")
    customer = models.ForeignKey("pos.Customer", null=True, blank=True, on_delete=models.SET_NULL, related_name="consignments")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT, related_name="consignments")
    reference = models.CharField(max_length=80, unique=True)
    status = models.CharField(max_length=30, choices=STATUS, default="open")
    settlement_due = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ConsignmentItem(models.Model):
    consignment = models.ForeignKey(Consignment, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("pos.Product", on_delete=models.PROTECT)
    quantity_received = models.DecimalField(max_digits=16, decimal_places=3)
    quantity_sold = models.DecimalField(max_digits=16, decimal_places=3, default=0)
    quantity_returned = models.DecimalField(max_digits=16, decimal_places=3, default=0)
    settlement_unit_price = models.DecimalField(max_digits=14, decimal_places=2, default=0)

class Currency(models.Model):
    business = models.ForeignKey("users.Business", on_delete=models.CASCADE, related_name="currencies")
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=80)
    symbol = models.CharField(max_length=8)
    decimal_places = models.PositiveSmallIntegerField(default=2)
    active = models.BooleanField(default=True)
    class Meta:
        constraints = [models.UniqueConstraint(fields=["business", "code"], name="unique_currency_per_business")]

class ExchangeRate(models.Model):
    business = models.ForeignKey("users.Business", on_delete=models.CASCADE, related_name="exchange_rates")
    base_currency = models.CharField(max_length=3)
    quote_currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=18, decimal_places=8)
    effective_at = models.DateTimeField()
    source = models.CharField(max_length=80, default="manual")
    class Meta:
        ordering = ["-effective_at"]

class ReceiptTemplate(models.Model):
    business = models.OneToOneField("users.Business", on_delete=models.CASCADE, related_name="receipt_template")
    title = models.CharField(max_length=160, default="Sales Receipt")
    footer = models.TextField(default="Thank you for your purchase!")
    paper_width = models.PositiveSmallIntegerField(default=80)
    show_logo = models.BooleanField(default=True)
    show_customer = models.BooleanField(default=True)
    show_cashier = models.BooleanField(default=True)

class RecognitionDataset(models.Model):
    business = models.ForeignKey("users.Business", on_delete=models.CASCADE, related_name="recognition_datasets")
    product = models.ForeignKey("pos.Product", on_delete=models.CASCADE, related_name="recognition_samples")
    image = models.ImageField(upload_to="recognition/%Y/%m/")
    label = models.CharField(max_length=160)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class RecognitionTrainingJob(models.Model):
    STATUS = [("queued","Queued"),("running","Running"),("completed","Completed"),("failed","Failed")]
    business = models.ForeignKey("users.Business", on_delete=models.CASCADE, related_name="recognition_jobs")
    status = models.CharField(max_length=20, choices=STATUS, default="queued")
    dataset_version = models.CharField(max_length=80, blank=True)
    model_version = models.CharField(max_length=80, blank=True)
    metrics = models.JSONField(default=dict, blank=True)
    error = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
