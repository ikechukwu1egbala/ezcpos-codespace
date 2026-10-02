from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from users.models import Business,Branch
from pos.models import Category,Product
class Command(BaseCommand):
 def handle(self,*args,**kwargs):
  U=get_user_model(); b,_=Business.objects.get_or_create(name='EZC Demo Store'); br,_=Branch.objects.get_or_create(business=b,name='Main Branch'); u=U.objects.filter(username='demo').first();
  if not u: u=U.objects.create_user(username='demo',password='demo1234',role='owner',business=b,branch=br); self.stdout.write('Created demo/demo1234')
  else: self.stdout.write('Demo user already exists')
  cat,_=Category.objects.get_or_create(name='General');
  for name,price in [('Milo 500g',4500),('Indomie Carton',12000),('Plantain Chips',1500)]: Product.objects.get_or_create(business=b,name=name,defaults={'category':cat,'selling_price':price,'buying_price':price*0.8,'sku':name[:6].upper()})
  self.stdout.write('Demo data ready.')
