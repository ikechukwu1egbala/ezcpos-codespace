from django.contrib import admin
from .models import Category,Product,Customer,Sale,SaleItem
admin.site.register([Category,Product,Customer,Sale,SaleItem])
