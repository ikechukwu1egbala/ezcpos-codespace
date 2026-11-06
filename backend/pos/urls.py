from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, CustomerViewSet, ProductViewSet, SaleViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="category")
router.register("products", ProductViewSet, basename="product")
router.register("customers", CustomerViewSet, basename="customer")
router.register("sales", SaleViewSet, basename="sale")

urlpatterns = router.urls
