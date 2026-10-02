from django.contrib.auth.models import AbstractUser
from django.db import models
class Business(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=40,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name
class Branch(models.Model):
    business=models.ForeignKey(Business,on_delete=models.CASCADE,related_name="branches")
    name=models.CharField(max_length=120)
    address=models.CharField(max_length=255,blank=True)
    active=models.BooleanField(default=True)
    def __str__(self): return f"{self.business.name} - {self.name}"
class User(AbstractUser):
    ROLE_CHOICES=[("owner","Owner"),("manager","Manager"),("staff","Staff")]
    business=models.ForeignKey(Business,null=True,blank=True,on_delete=models.SET_NULL,related_name="users")
    branch=models.ForeignKey(Branch,null=True,blank=True,on_delete=models.SET_NULL,related_name="users")
    role=models.CharField(max_length=20,choices=ROLE_CHOICES,default="staff")
