from django.conf import settings
from django.db import models
class Device(models.Model):
 business=models.ForeignKey("users.Business",on_delete=models.CASCADE)
 device_id=models.CharField(max_length=120)
 name=models.CharField(max_length=120,blank=True)
 last_seen=models.DateTimeField(auto_now=True)
 active=models.BooleanField(default=True)
 class Meta: unique_together=("business","device_id")
class SyncOperation(models.Model):
 STATUS=[("processed","Processed"),("failed","Failed")]
 operation_id=models.UUIDField(unique=True)
 business=models.ForeignKey("users.Business",on_delete=models.CASCADE)
 device=models.ForeignKey(Device,null=True,blank=True,on_delete=models.SET_NULL)
 operation_type=models.CharField(max_length=50)
 payload=models.JSONField(default=dict)
 status=models.CharField(max_length=20,choices=STATUS,default="processed")
 error=models.TextField(blank=True)
 created_at=models.DateTimeField(auto_now_add=True)
 processed_at=models.DateTimeField(null=True,blank=True)
