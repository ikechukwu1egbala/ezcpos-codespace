from decimal import Decimal
from django.conf import settings
from django.db import models
class Category(models.Model): name=models.CharField(max_length=120,unique=True)
class Product(models.Model):
    business=models.ForeignKey("users.Business",on_delete=models.CASCADE,related_name="products")
    category=models.ForeignKey(Category,null=True,blank=True,on_delete=models.SET_NULL)
    name=models.CharField(max_length=200)
    sku=models.CharField(max_length=80,blank=True)
    barcode=models.CharField(max_length=100,blank=True)
    buying_price=models.DecimalField(max_digits=14,decimal_places=2,default=0)
    selling_price=models.DecimalField(max_digits=14,decimal_places=2,default=0)
    unit=models.CharField(max_length=30,default="piece")
    low_stock_level=models.DecimalField(max_digits=14,decimal_places=3,default=0)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name
class Customer(models.Model):
    business=models.ForeignKey("users.Business",on_delete=models.CASCADE,related_name="customers")
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=40,blank=True)
    address=models.CharField(max_length=255,blank=True)
    credit_balance=models.DecimalField(max_digits=14,decimal_places=2,default=0)
class Sale(models.Model):
    PAYMENT_STATUS=[("unpaid","Unpaid"),("partial","Partial"),("paid","Paid"),("refunded","Refunded")]
    business=models.ForeignKey("users.Business",on_delete=models.CASCADE,related_name="sales")
    branch=models.ForeignKey("users.Branch",null=True,blank=True,on_delete=models.SET_NULL)
    cashier=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    customer=models.ForeignKey(Customer,null=True,blank=True,on_delete=models.SET_NULL)
    subtotal=models.DecimalField(max_digits=14,decimal_places=2)
    discount=models.DecimalField(max_digits=14,decimal_places=2,default=0)
    total=models.DecimalField(max_digits=14,decimal_places=2)
    amount_paid=models.DecimalField(max_digits=14,decimal_places=2,default=0)
    payment_status=models.CharField(max_length=20,choices=PAYMENT_STATUS,default="unpaid")
    operation_id=models.UUIDField(unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
class SaleItem(models.Model):
    sale=models.ForeignKey(Sale,on_delete=models.CASCADE,related_name="items")
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.DecimalField(max_digits=14,decimal_places=3)
    unit_price=models.DecimalField(max_digits=14,decimal_places=2)
    line_total=models.DecimalField(max_digits=14,decimal_places=2)
