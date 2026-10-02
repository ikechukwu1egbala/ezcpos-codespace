from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *

class BusinessScopedMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        business = getattr(self.request.user, "business", None)
        return qs.filter(business=business) if business else qs.none()
    def perform_create(self, serializer):
        serializer.save(business=self.request.user.business)

class SupplierViewSet(BusinessScopedMixin, viewsets.ModelViewSet): queryset=Supplier.objects.all(); serializer_class=SupplierSerializer
class WarehouseViewSet(BusinessScopedMixin, viewsets.ModelViewSet): queryset=Warehouse.objects.all(); serializer_class=WarehouseSerializer
class WarehouseStockViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class=WarehouseStockSerializer
    def get_queryset(self): return WarehouseStock.objects.filter(warehouse__business=getattr(self.request.user,"business",None))
class StockTransferViewSet(BusinessScopedMixin, viewsets.ModelViewSet):
    queryset=StockTransfer.objects.all(); serializer_class=StockTransferSerializer
    @action(detail=True, methods=["post"])
    def ship(self, request, pk=None):
        obj=self.get_object(); obj.status="in_transit"; obj.shipped_at=timezone.now(); obj.save(update_fields=["status","shipped_at"]); return Response(self.get_serializer(obj).data)
    @action(detail=True, methods=["post"])
    def receive(self, request, pk=None):
        obj=self.get_object(); obj.status="received"; obj.received_at=timezone.now(); obj.save(update_fields=["status","received_at"]); return Response(self.get_serializer(obj).data)
class ConsignmentViewSet(BusinessScopedMixin, viewsets.ModelViewSet): queryset=Consignment.objects.all(); serializer_class=ConsignmentSerializer
class CurrencyViewSet(BusinessScopedMixin, viewsets.ModelViewSet): queryset=Currency.objects.all(); serializer_class=CurrencySerializer
class ExchangeRateViewSet(BusinessScopedMixin, viewsets.ModelViewSet): queryset=ExchangeRate.objects.all(); serializer_class=ExchangeRateSerializer
class ReceiptTemplateViewSet(BusinessScopedMixin, viewsets.ModelViewSet): queryset=ReceiptTemplate.objects.all(); serializer_class=ReceiptTemplateSerializer
class RecognitionDatasetViewSet(BusinessScopedMixin, viewsets.ModelViewSet): queryset=RecognitionDataset.objects.all(); serializer_class=RecognitionDatasetSerializer
class RecognitionTrainingJobViewSet(BusinessScopedMixin, viewsets.ReadOnlyModelViewSet): queryset=RecognitionTrainingJob.objects.all(); serializer_class=RecognitionTrainingJobSerializer

from django.http import HttpResponse
from .services.receipts import render_receipt_html

class ReceiptPreviewViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        from pos.models import Sale
        sale = Sale.objects.select_related("business").filter(pk=pk, business=getattr(request.user,"business",None)).first()
        if not sale: return Response({"detail":"Not found"}, status=status.HTTP_404_NOT_FOUND)
        return HttpResponse(render_receipt_html(sale), content_type="text/html")
