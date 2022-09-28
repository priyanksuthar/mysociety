from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from event.models import Event
from event.serializers import EventSerializer
from mysociety.utils.response import APIResponse
# Create your views here.


class EventAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, event_id=None):
        if event_id:
            try:
                obj = Event.objects.get(id=event_id)
                ser_obj = EventSerializer(obj)
            except Exception:
                return APIResponse(status_code=404, error="data not found for event").json_response()
        else:
            objs = Event.objects.all()
            ser_obj = EventSerializer(objs, many=True)
        return APIResponse(status_code=200, success=True, body={"data": ser_obj.data}).json_response()

    def post(self, request):
        data = request.data
        ser_obj = EventSerializer(data=data)
        if ser_obj.is_valid():
            ser_obj.save(created_by=request.user, modified_by=request.user)
            return APIResponse(status_code=201, success=True, body={"data": ser_obj.data}).json_response()
        else:
            return APIResponse(status_code=400, error=ser_obj.errors).json_response()

    def put(self, request, event_id=None):
        data = request.data
        try:
            obj = Event.objects.get(id=event_id)
        except Exception:
            return APIResponse(status_code=404, error="data not found for event id").json_response()

        ser_obj = EventSerializer(obj, data=data)
        if ser_obj.is_valid():
            ser_obj.save(modified_by=request.user)
            return APIResponse(status_code=200, success=True, body={"data": ser_obj.data}).json_response()
        else:
            return APIResponse(status_code=400, error=ser_obj.errors).json_response()