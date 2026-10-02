from rest_framework import viewsets
from .models import Payment,Refund
from .serializers import PaymentSerializer,RefundSerializer
class PaymentViewSet(viewsets.ReadOnlyModelViewSet):
 serializer_class=PaymentSerializer
 def get_queryset(self): return Payment.objects.filter(business=self.request.user.business).order_by("-created_at")
class RefundViewSet(viewsets.ModelViewSet):
 serializer_class=RefundSerializer
 def get_queryset(self): return Refund.objects.filter(business=self.request.user.business).order_by("-created_at")
 def perform_create(self,serializer): serializer.save(business=self.request.user.business)
