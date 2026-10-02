from rest_framework.routers import DefaultRouter
from .views import BusinessViewSet,BranchViewSet
r=DefaultRouter(); r.register("businesses",BusinessViewSet,basename="business"); r.register("branches",BranchViewSet,basename="branch")
urlpatterns=r.urls
