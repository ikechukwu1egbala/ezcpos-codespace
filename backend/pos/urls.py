from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet,ProductViewSet,CustomerViewSet,SaleViewSet
r=DefaultRouter(); r.register("categories",CategoryViewSet); r.register("products",ProductViewSet); r.register("customers",CustomerViewSet); r.register("sales",SaleViewSet,basename="sale")
urlpatterns=r.urls
