from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Category,Product,Customer,Sale
from .serializers import CategorySerializer,ProductSerializer,CustomerSerializer,SaleSerializer
def biz(qs,user): return qs.filter(business=user.business)
class CategoryViewSet(viewsets.ModelViewSet):
 serializer_class=CategorySerializer
 def get_queryset(self): return Category.objects.filter(products__business=self.request.user.business).distinct()
class ProductViewSet(viewsets.ModelViewSet):
 serializer_class=ProductSerializer
 def get_queryset(self): return Product.objects.filter(business=self.request.user.business).select_related("category")
class CustomerViewSet(viewsets.ModelViewSet):
 serializer_class=CustomerSerializer
 def get_queryset(self): return Customer.objects.filter(business=self.request.user.business)
class SaleViewSet(viewsets.ReadOnlyModelViewSet):
 serializer_class=SaleSerializer
 def get_queryset(self): return Sale.objects.filter(business=self.request.user.business).prefetch_related("items").order_by("-created_at")
 @action(detail=False,methods=["get"])
 def summary(self,request):
  q=self.get_queryset(); return Response({"sales_count":q.count(),"total_sales":q.aggregate(v=Sum("total"))["v"] or 0})
