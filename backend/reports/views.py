from django.db.models import Sum,Count
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from pos.models import Sale
from expenses.models import Expense
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard(request):
 s=Sale.objects.filter(business=request.user.business); e=Expense.objects.filter(business=request.user.business)
 return Response({"sales_count":s.count(),"sales_total":s.aggregate(v=Sum("total"))["v"] or 0,"expenses_total":e.aggregate(v=Sum("amount"))["v"] or 0,"customers":request.user.business.customers.count(),"products":request.user.business.products.count()})
