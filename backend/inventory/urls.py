from rest_framework.routers import DefaultRouter
from .views import InventoryBalanceViewSet,InventoryMovementViewSet
r=DefaultRouter(); r.register("inventory",InventoryBalanceViewSet,basename="inventory"); r.register("inventory-movements",InventoryMovementViewSet,basename="inventory-movement")
urlpatterns=r.urls
