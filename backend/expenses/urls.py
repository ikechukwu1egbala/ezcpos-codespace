from rest_framework.routers import DefaultRouter
from .views import ExpenseCategoryViewSet,ExpenseViewSet
r=DefaultRouter(); r.register("expense-categories",ExpenseCategoryViewSet,basename="expense-category"); r.register("expenses",ExpenseViewSet,basename="expense")
urlpatterns=r.urls
