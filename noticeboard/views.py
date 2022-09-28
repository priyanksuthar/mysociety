from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from noticeboard.models import NoticeBoard, NoticeStatus
from noticeboard.serializers import NoticeBoardSerializer, NoticeStatusSerializer
from mysociety.utils.response import APIResponse
# Create your views here.


class NoticeBoardAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, notice_id=None):
        if notice_id:
            try:
                obj = NoticeBoard.objects.get(id=notice_id)
                ser_obj = NoticeBoardSerializer(obj)
            except Exception:
                return APIResponse(status_code=404, error="data not found for building").json_response()
        else:
            objs = NoticeBoard.objects.all()
            ser_obj = NoticeBoardSerializer(objs, many=True)
        return APIResponse(status_code=200, success=True, body={"data": ser_obj.data}).json_response()

    def post(self, request):
        data = request.data
        data["created_by"] = request.user.id
        ser_obj = NoticeBoardSerializer(data=data)
        if ser_obj.is_valid():
            ser_obj.save(created_by=request.user, modified_by=request.user)
            return APIResponse(status_code=201, success=True, body={"data": ser_obj.data}).json_response()
        else:
            return APIResponse(status_code=400, error=ser_obj.errors).json_response()

    def put(self, request, notice_id=None):
        data = request.data
        data["created_by"] = request.user.id
        try:
            obj = NoticeBoard.objects.get(id=notice_id)
        except Exception:
            return APIResponse(status_code=404, error="data not found for wing id").json_response()

        ser_obj = NoticeBoardSerializer(obj, data=data)
        if ser_obj.is_valid():
            ser_obj.save(modified_by=request.user)
            return APIResponse(status_code=200, success=True, body={"data": ser_obj.data}).json_response()
        else:
            return APIResponse(status_code=400, error=ser_obj.errors).json_response()


class NoticeStatusAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, status_id=None):
        if status_id:
            try:
                obj = NoticeStatus.objects.get(id=status_id)
                ser_obj = NoticeStatusSerializer(obj)
            except Exception:
                return APIResponse(status_code=404, error="data not found for building").json_response()
        else:
            objs = NoticeStatus.objects.all()
            ser_obj = NoticeStatusSerializer(objs, many=True)
        return APIResponse(status_code=200, success=True, body={"data": ser_obj.data}).json_response()

    def post(self, request):
        data = request.data
        ser_obj = NoticeStatusSerializer(data=data)
        if ser_obj.is_valid():
            ser_obj.save()
            return APIResponse(status_code=201, success=True, body={"data": ser_obj.data}).json_response()
        else:
            return APIResponse(status_code=400, error=ser_obj.errors).json_response()

    def put(self, request, status_id=None):
        data = request.data
        try:
            obj = NoticeStatus.objects.get(id=status_id)
        except Exception:
            return APIResponse(status_code=404, error="data not found for wing id").json_response()

        ser_obj = NoticeStatusSerializer(obj, data=data)
        if ser_obj.is_valid():
            ser_obj.save()
            return APIResponse(status_code=200, success=True, body={"data": ser_obj.data}).json_response()
        else:
            return APIResponse(status_code=400, error=ser_obj.errors).json_response()
