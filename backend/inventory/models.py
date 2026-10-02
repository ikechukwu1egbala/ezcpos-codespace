from django.db import models
class InventoryBalance(models.Model):
 business=models.ForeignKey("users.Business",on_delete=models.CASCADE)
 branch=models.ForeignKey("users.Branch",null=True,on_delete=models.CASCADE)
 product=models.ForeignKey("pos.Product",on_delete=models.CASCADE)
 quantity=models.DecimalField(max_digits=14,decimal_places=3,default=0)
 class Meta: unique_together=("business","branch","product")
class InventoryMovement(models.Model):
 TYPES=[("sale","Sale"),("return","Return"),("restock","Restock"),("adjustment","Adjustment")]
 business=models.ForeignKey("users.Business",on_delete=models.CASCADE)
 branch=models.ForeignKey("users.Branch",null=True,on_delete=models.SET_NULL)
 product=models.ForeignKey("pos.Product",on_delete=models.PROTECT)
 quantity_delta=models.DecimalField(max_digits=14,decimal_places=3)
 movement_type=models.CharField(max_length=20,choices=TYPES)
 reference=models.CharField(max_length=100,blank=True)
 created_at=models.DateTimeField(auto_now_add=True)
