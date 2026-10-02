from rest_framework import viewsets
from .models import InventoryBalance,InventoryMovement
from .serializers import InventoryBalanceSerializer,InventoryMovementSerializer
class InventoryBalanceViewSet(viewsets.ReadOnlyModelViewSet):
 serializer_class=InventoryBalanceSerializer
 def get_queryset(self): return InventoryBalance.objects.filter(business=self.request.user.business)
class InventoryMovementViewSet(viewsets.ReadOnlyModelViewSet):
 serializer_class=InventoryMovementSerializer
 def get_queryset(self): return InventoryMovement.objects.filter(business=self.request.user.business).order_by("-created_at")
