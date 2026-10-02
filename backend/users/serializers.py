from rest_framework import serializers
from .models import User,Business,Branch
class UserSerializer(serializers.ModelSerializer):
    class Meta: model=User; fields=["id","username","first_name","last_name","role","business_id","branch_id"]
class BusinessSerializer(serializers.ModelSerializer):
    class Meta: model=Business; fields="__all__"
class BranchSerializer(serializers.ModelSerializer):
    class Meta: model=Branch; fields="__all__"
