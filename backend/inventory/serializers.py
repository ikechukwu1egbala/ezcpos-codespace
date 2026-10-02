from rest_framework import serializers
from .models import InventoryBalance,InventoryMovement
class InventoryBalanceSerializer(serializers.ModelSerializer):
 class Meta: model=InventoryBalance; fields="__all__"
class InventoryMovementSerializer(serializers.ModelSerializer):
 class Meta: model=InventoryMovement; fields="__all__"
