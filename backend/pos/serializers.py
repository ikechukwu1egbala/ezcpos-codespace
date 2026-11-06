from decimal import Decimal

from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Category, Customer, Product, Sale, SaleItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "business"]


class ProductSerializer(serializers.ModelSerializer):
    stock_quantity = serializers.DecimalField(max_digits=14, decimal_places=3, min_value=0, required=False)

    class Meta:
        model = Product
        fields = [
            "id",
            "business",
            "category",
            "category_name",
            "name",
            "sku",
            "barcode",
            "buying_price",
            "selling_price",
            "unit",
            "stock_quantity",
            "low_stock_level",
            "active",
            "created_at",
        ]
        read_only_fields = ["id", "business", "created_at"]

    category_name = serializers.SerializerMethodField()

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None

    def validate(self, attrs):
        qty = attrs.get("stock_quantity")
        if qty is not None and qty < 0:
            raise ValidationError({"stock_quantity": "Stock cannot be negative."})
        return attrs


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "business", "name", "phone", "address", "credit_balance"]
        read_only_fields = ["id", "business"]


class SaleItemSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    unit_price = serializers.DecimalField(max_digits=14, decimal_places=2, min_value=0)

    class Meta:
        model = SaleItem
        fields = ["id", "product", "product_name", "quantity", "unit_price", "line_total"]
        read_only_fields = ["id", "product_name", "line_total"]

    def get_product_name(self, obj):
        return obj.product.name if obj.product else None


class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True, read_only=True)

    class Meta:
        model = Sale
        fields = [
            "id",
            "business",
            "branch",
            "cashier",
            "customer",
            "subtotal",
            "discount",
            "total",
            "amount_paid",
            "payment_status",
            "operation_id",
            "created_at",
            "items",
        ]
        read_only_fields = ["id", "business", "cashier", "operation_id", "created_at", "items"]

    def validate(self, attrs):
        if not attrs.get("items"):
            raise ValidationError({"items": "At least one item is required."})
        return attrs
