from rest_framework import viewsets
from .models import ExpenseCategory,Expense
from .serializers import ExpenseCategorySerializer,ExpenseSerializer
class ExpenseCategoryViewSet(viewsets.ModelViewSet):
 serializer_class=ExpenseCategorySerializer
 def get_queryset(self): return ExpenseCategory.objects.filter(business=self.request.user.business)
 def perform_create(self,s): s.save(business=self.request.user.business)
class ExpenseViewSet(viewsets.ModelViewSet):
 serializer_class=ExpenseSerializer
 def get_queryset(self): return Expense.objects.filter(business=self.request.user.business).order_by("-created_at")
 def perform_create(self,s): s.save(business=self.request.user.business)
