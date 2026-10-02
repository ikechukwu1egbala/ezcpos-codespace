from django.contrib import admin
from .models import InventoryBalance,InventoryMovement
admin.site.register([InventoryBalance,InventoryMovement])
