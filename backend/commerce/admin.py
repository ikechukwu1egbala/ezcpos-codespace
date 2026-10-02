from django.contrib import admin
from .models import *
for model in [Supplier, Warehouse, WarehouseStock, StockTransfer, StockTransferItem, Consignment, ConsignmentItem, Currency, ExchangeRate, ReceiptTemplate, RecognitionDataset, RecognitionTrainingJob]:
    admin.site.register(model)
