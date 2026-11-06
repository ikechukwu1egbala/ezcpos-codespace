from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.views import health

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/health/", health),
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/users/", include("users.urls")),
    path("api/pos/", include("pos.urls")),
    path("api/inventory/", include("inventory.urls")),
    path("api/payments/", include("payments.urls")),
    path("api/expenses/", include("expenses.urls")),
    path("api/reports/", include("reports.urls")),
    path("api/sync/", include("sync.urls")),
    path("api/commerce/", include("commerce.urls")),
]
