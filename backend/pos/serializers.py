from rest_framework import serializers
from .models import Category,Product,Customer,Sale,SaleItem
class CategorySerializer(serializers.ModelSerializer):
 class Meta: model=Category; fields="__all__"
class ProductSerializer(serializers.ModelSerializer):
 class Meta: model=Product; fields="__all__"
class CustomerSerializer(serializers.ModelSerializer):
 class Meta: model=Customer; fields="__all__"
class SaleItemSerializer(serializers.ModelSerializer):
 class Meta: model=SaleItem; fields=["id","product","quantity","unit_price","line_total"]
class SaleSerializer(serializers.ModelSerializer):
 items=SaleItemSerializer(many=True,read_only=True)
 class Meta: model=Sale; fields="__all__"
