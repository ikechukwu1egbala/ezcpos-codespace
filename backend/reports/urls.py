from django.urls import path
from .views import dashboard
urlpatterns=[path("reports/dashboard/",dashboard)]
