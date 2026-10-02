from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SyncOperation
from .serializers import SyncOperationSerializer
class SyncPushView(APIView):
 def post(self,request):
  results=[]
  for item in request.data.get("operations",[]):
   oid=item.get("operation_id")
   if not oid: results.append({"status":"failed","error":"operation_id required"}); continue
   existing=SyncOperation.objects.filter(operation_id=oid,business=request.user.business).first()
   if existing: results.append({"operation_id":str(existing.operation_id),"status":"already_processed"}); continue
   op=SyncOperation.objects.create(operation_id=oid,business=request.user.business,operation_type=item.get("operation_type","unknown"),payload=item.get("payload",{}),status="processed",processed_at=timezone.now())
   results.append({"operation_id":str(op.operation_id),"status":"processed"})
  return Response({"results":results},status=status.HTTP_200_OK)
class SyncPullView(APIView):
 def get(self,request):
  qs=SyncOperation.objects.filter(business=request.user.business).order_by("created_at")
  return Response({"operations":SyncOperationSerializer(qs,many=True).data})
