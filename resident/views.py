from django.shortcuts import render
from django.http.response import Http404
import json
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from resident.models import Buildings, Wings, Flats
from resident.serializers import BuildingSerializer, WingSerializer, FlatSerializer
from mysociety.utils.response import APIResponse
# Create your views here.


class BuildingsAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get(self, request, building_id=None):
        if building_id:
            try:
                obj = Buildings.objects.get(id=building_id)
                ser_obj = BuildingSerializer(obj)
            except Exception:
                return APIResponse(status_code=404, error="data not found for building id").json_response()
        else:
            objs = Buildings.objects.all()
            ser_obj = BuildingSerializer(objs, many=True)
        return APIResponse(status_code=200, success=True, body={"data": ser_obj.data}).json_response()

    def post(self, request):
        data = request.data
        ser_obj = BuildingSerializer(data=data)
        if ser_obj.is_valid():
            ser_obj.save()
            return APIResponse(status_code=201, success=True, body={"data": ser_obj.data}).json_response()
        else:
            return APIResponse(status_code=400, error=ser_obj.errors).json_response()

    def put(self, request, building_id=None):
        data = request.data
        try:
            obj = Buildings.objects.get(id=building_id)
        except Exception:
            return APIResponse(status_code=404, error="data not found for building id").json_response()

        ser_obj = BuildingSerializer(obj, data=data)
        if ser_obj.is_valid():
            ser_obj.save()
            return APIResponse(status_code=200, success=True, body={"data": ser_obj.data}).json_response()
        else:
            return APIResponse(status_code=400, error=ser_obj.errors).json_response()


class WingsAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get(self, request, wing_id=None):
        if wing_id:
            try:
                obj = Wings.objects.get(id=wing_id)
                ser_obj = WingSerializer(obj)
            except Exception:
                return APIResponse(status_code=404, error="data not found for wing id").json_response()
        else:
            objs = Wings.objects.all()
            ser_obj = WingSerializer(objs, many=True)
        return APIResponse(status_code=200, success=True, body={"data": ser_obj.data}).json_response()

    def post(self, request):
        data = request.data
        ser_obj = WingSerializer(data=data)
        if ser_obj.is_valid():
            ser_obj.save()
            return APIResponse(status_code=201, success=True, body={"data": ser_obj.data}).json_response()
        else:
            return APIResponse(status_code=400, error=ser_obj.errors).json_response()

    def put(self, request, wing_id=None):
        data = request.data
        try:
            obj = Wings.objects.get(id=wing_id)
        except Exception:
            return APIResponse(status_code=404, error="data not found for wing id").json_response()

        ser_obj = WingSerializer(obj, data=data)
        if ser_obj.is_valid():
            ser_obj.save()
            return APIResponse(status_code=200, success=True, body={"data": ser_obj.data}).json_response()
        else:
            return APIResponse(status_code=400, error=ser_obj.errors).json_response()


class FlatAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get(self, request, flat_id=None):
        if flat_id:
            try:
                obj = Flats.objects.get(id=flat_id)
                ser_obj = FlatSerializer(obj)
            except Exception:
                return APIResponse(status_code=404, error="data not found for flat id").json_response()
        else:
            objs = Flats.objects.all()
            ser_obj = FlatSerializer(objs, many=True)
        return APIResponse(status_code=200, success=True, body={"data": ser_obj.data}).json_response()

    def post(self, request):
        data = request.data
        ser_obj = FlatSerializer(data=data)
        if ser_obj.is_valid():
            ser_obj.save(created_by=request.user, modified_by=request.user)
            return APIResponse(status_code=201, success=True, body={"data": ser_obj.data}).json_response()
        else:
            return APIResponse(status_code=400, error=ser_obj.errors).json_response()

    def put(self, request, flat_id=None):
        data = request.data
        try:
            obj = Flats.objects.get(id=flat_id)
        except Exception:
            return APIResponse(status_code=404, error="data not found for flat id").json_response()

        ser_obj = FlatSerializer(obj, data=data)
        if ser_obj.is_valid():
            ser_obj.save(modified_by=request.user)
            return APIResponse(status_code=200, success=True, body={"data": ser_obj.data}).json_response()
        else:
            return APIResponse(status_code=400, error=ser_obj.errors).json_response()

