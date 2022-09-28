from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from mysociety.utils.response import APIResponse
from committee.models import Committees, CommitteeMembers, CommitteeRoles
from committee.serializers import CommitteeSerializer, CommitteeRoleSerializer, \
    CommitteeMemberSerializer
# Create your views here.


class CommitteeAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get(self, request, committee_id=None):
        if committee_id:
            try:
                obj = Committees.objects.get(id=committee_id)
                ser_obj = CommitteeSerializer(obj)
            except Exception:
                return APIResponse(status_code=404, error="data not found for committee id").json_response()
        else:
            objs = Committees.objects.all()
            ser_obj = CommitteeSerializer(objs, many=True)
        return APIResponse(status_code=200, success=True, body={"data": ser_obj.data}).json_response()

    def post(self, request):
        data = request.data
        ser_obj = CommitteeSerializer(data=data)
        if ser_obj.is_valid():
            ser_obj.save()
            return APIResponse(status_code=201, success=True, body={"data": ser_obj.data}).json_response()
        else:
            return APIResponse(status_code=400, error=ser_obj.errors).json_response()

    def put(self, request, committee_id=None):
        data = request.data
        try:
            obj = Committees.objects.get(id=committee_id)
        except Exception:
            return APIResponse(status_code=404, error="data not found for committee id").json_response()

        ser_obj = CommitteeSerializer(obj, data=data)
        if ser_obj.is_valid():
            ser_obj.save(modified_by=request.user)
            return APIResponse(status_code=200, success=True, body={"data": ser_obj.data}).json_response()
        else:
            return APIResponse(status_code=400, error=ser_obj.errors).json_response()


class CommitteeRoleAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get(self, request, role_id=None):
        if role_id:
            try:
                obj = CommitteeRoles.objects.get(id=role_id)
                ser_obj = CommitteeRoleSerializer(obj)
            except Exception:
                return APIResponse(status_code=404, error="data not found for committee role id").json_response()
        else:
            objs = CommitteeRoles.objects.all()
            ser_obj = CommitteeRoleSerializer(objs, many=True)
        return APIResponse(status_code=200, success=True, body={"data": ser_obj.data}).json_response()

    def post(self, request):
        data = request.data
        ser_obj = CommitteeRoleSerializer(data=data)
        if ser_obj.is_valid():
            ser_obj.save(created_by=request.user, modified_by=request.user)
            return APIResponse(status_code=201, success=True, body={"data": ser_obj.data}).json_response()
        else:
            return APIResponse(status_code=400, error=ser_obj.errors).json_response()

    def put(self, request, role_id=None):
        data = request.data
        try:
            obj = CommitteeRoles.objects.get(id=role_id)
        except Exception:
            return APIResponse(status_code=404, error="data not found for committee role id").json_response()

        ser_obj = CommitteeRoleSerializer(obj, data=data)
        if ser_obj.is_valid():
            ser_obj.save(modified_by=request.user)
            return APIResponse(status_code=200, success=True, body={"data": ser_obj.data}).json_response()
        else:
            return APIResponse(status_code=400, error=ser_obj.errors).json_response()


class CommitteeMemberAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get(self, request, member_id=None):
        if member_id:
            try:
                obj = CommitteeMembers.objects.get(id=member_id)
                ser_obj = CommitteeMemberSerializer(obj)
            except Exception:
                return APIResponse(status_code=404, error="data not found for committee member id").json_response()
        else:
            objs = CommitteeMembers.objects.all()
            ser_obj = CommitteeMemberSerializer(objs, many=True)
        return APIResponse(status_code=200, success=True, body={"data": ser_obj.data}).json_response()

    def post(self, request):
        data = request.data
        ser_obj = CommitteeMemberSerializer(data=data)
        if ser_obj.is_valid():
            ser_obj.save(created_by=request.user, modified_by=request.user)
            return APIResponse(status_code=201, success=True, body={"data": ser_obj.data}).json_response()
        else:
            return APIResponse(status_code=400, error=ser_obj.errors).json_response()

    def put(self, request, member_id=None):
        data = request.data
        try:
            obj = CommitteeMembers.objects.get(id=member_id)
        except Exception:
            return APIResponse(status_code=404, error="data not found for committee member id").json_response()

        ser_obj = CommitteeMemberSerializer(obj, data=data)
        if ser_obj.is_valid():
            ser_obj.save(modified_by=request.user)
            return APIResponse(status_code=200, success=True, body={"data": ser_obj.data}).json_response()
        else:
            return APIResponse(status_code=400, error=ser_obj.errors).json_response()