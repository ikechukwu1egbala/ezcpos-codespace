from rest_framework import viewsets
from .models import Business,Branch
from .serializers import BusinessSerializer,BranchSerializer
class BusinessViewSet(viewsets.ModelViewSet):
    serializer_class=BusinessSerializer
    def get_queryset(self): return Business.objects.filter(users=self.request.user)
class BranchViewSet(viewsets.ModelViewSet):
    serializer_class=BranchSerializer
    def get_queryset(self): return Branch.objects.filter(business=self.request.user.business)
