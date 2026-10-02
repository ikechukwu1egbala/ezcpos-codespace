from django.db import models
class ExpenseCategory(models.Model):
 business=models.ForeignKey("users.Business",on_delete=models.CASCADE)
 name=models.CharField(max_length=120)
class Expense(models.Model):
 business=models.ForeignKey("users.Business",on_delete=models.CASCADE)
 category=models.ForeignKey(ExpenseCategory,null=True,blank=True,on_delete=models.SET_NULL)
 amount=models.DecimalField(max_digits=14,decimal_places=2)
 description=models.CharField(max_length=255,blank=True)
 created_at=models.DateTimeField(auto_now_add=True)
