from rest_framework.routers import DefaultRouter
from .views import *
router=DefaultRouter()
router.register("suppliers", SupplierViewSet)
router.register("warehouses", WarehouseViewSet)
router.register("warehouse-stock", WarehouseStockViewSet, basename="warehouse-stock")
router.register("transfers", StockTransferViewSet)
router.register("consignments", ConsignmentViewSet)
router.register("currencies", CurrencyViewSet)
router.register("exchange-rates", ExchangeRateViewSet)
router.register("receipt-template", ReceiptTemplateViewSet)
router.register("recognition-datasets", RecognitionDatasetViewSet)
router.register("recognition-jobs", RecognitionTrainingJobViewSet)
urlpatterns=router.urls
from django.urls import path
from .views import ReceiptPreviewViewSet
urlpatterns += [path("receipts/<int:pk>/", ReceiptPreviewViewSet.as_view({"get":"retrieve"}), name="receipt-preview")]
