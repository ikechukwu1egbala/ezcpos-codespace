from django.db import models
class Payment(models.Model):
 METHODS=[("cash","Cash"),("card","Card"),("transfer","Transfer"),("split","Split")]
 business=models.ForeignKey("users.Business",on_delete=models.CASCADE)
 sale=models.ForeignKey("pos.Sale",on_delete=models.CASCADE,related_name="payments")
 amount=models.DecimalField(max_digits=14,decimal_places=2)
 method=models.CharField(max_length=20,choices=METHODS)
 reference=models.CharField(max_length=120,blank=True)
 created_at=models.DateTimeField(auto_now_add=True)
class Refund(models.Model):
 business=models.ForeignKey("users.Business",on_delete=models.CASCADE)
 sale=models.ForeignKey("pos.Sale",on_delete=models.PROTECT)
 amount=models.DecimalField(max_digits=14,decimal_places=2)
 reason=models.CharField(max_length=255,blank=True)
 created_at=models.DateTimeField(auto_now_add=True)
