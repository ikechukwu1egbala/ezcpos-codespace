from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet,RefundViewSet
r=DefaultRouter(); r.register("payments",PaymentViewSet,basename="payment"); r.register("refunds",RefundViewSet,basename="refund")
urlpatterns=r.urls
