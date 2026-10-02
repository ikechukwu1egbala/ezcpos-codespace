from rest_framework import serializers
from .models import *

class SupplierSerializer(serializers.ModelSerializer):
    class Meta: model = Supplier; fields = "__all__"
class WarehouseSerializer(serializers.ModelSerializer):
    class Meta: model = Warehouse; fields = "__all__"
class WarehouseStockSerializer(serializers.ModelSerializer):
    class Meta: model = WarehouseStock; fields = "__all__"
class StockTransferItemSerializer(serializers.ModelSerializer):
    class Meta: model = StockTransferItem; fields = "__all__"
class StockTransferSerializer(serializers.ModelSerializer):
    items = StockTransferItemSerializer(many=True, read_only=True)
    class Meta: model = StockTransfer; fields = "__all__"
class ConsignmentItemSerializer(serializers.ModelSerializer):
    class Meta: model = ConsignmentItem; fields = "__all__"
class ConsignmentSerializer(serializers.ModelSerializer):
    items = ConsignmentItemSerializer(many=True, read_only=True)
    class Meta: model = Consignment; fields = "__all__"
class CurrencySerializer(serializers.ModelSerializer):
    class Meta: model = Currency; fields = "__all__"
class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta: model = ExchangeRate; fields = "__all__"
class ReceiptTemplateSerializer(serializers.ModelSerializer):
    class Meta: model = ReceiptTemplate; fields = "__all__"
class RecognitionDatasetSerializer(serializers.ModelSerializer):
    class Meta: model = RecognitionDataset; fields = "__all__"
class RecognitionTrainingJobSerializer(serializers.ModelSerializer):
    class Meta: model = RecognitionTrainingJob; fields = "__all__"
