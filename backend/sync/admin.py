from django.contrib import admin
from .models import Device,SyncOperation
admin.site.register([Device,SyncOperation])
