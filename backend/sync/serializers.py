from rest_framework import serializers
from .models import SyncOperation
class SyncOperationSerializer(serializers.ModelSerializer):
 class Meta: model=SyncOperation; fields=["operation_id","operation_type","payload","status","error","created_at","processed_at"]
