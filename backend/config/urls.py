from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.views import health
urlpatterns=[
    path("api/commerce/", include("commerce.urls")),path("admin/",admin.site.urls),path("api/health/",health),path("api/auth/token/",TokenObtainPairView.as_view()),path("api/auth/token/refresh/",TokenRefreshView.as_view()),path("api/users/",include("users.urls")),path("api/",include("pos.urls")),path("api/",include("inventory.urls")),path("api/",include("payments.urls")),path("api/",include("expenses.urls")),path("api/",include("reports.urls")),path("api/",include("sync.urls"))]
