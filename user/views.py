from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from user.models import User
from user.serializers import UserSerializer
from mysociety.utils.response import APIResponse
# Create your views here.


class UserApi(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_id = request.query_params.get("user_id", "")

        if user_id:
            objs = User.objects.filter(id=user_id)
        else:
            objs = User.objects.filter()

        res_data = []
        for obj in objs:
            res_data.append(generate_user_obj(obj))

        res = APIResponse()
        res.status_code = 200
        res.success = True
        res.body = res_data
        return res.json_response()

    def post(self, request):
        email = request.data.get("email", "")
        password = request.data.get("password", "")
        res = APIResponse()
        if not email:
            res.status_code = 400
            res.error = "email should not be empty"
        if not password:
            res.status_code = 400
            res.error = "password should not be empty"
        if not len(password) > 7:
            res.status_code = 400
            res.error = "password length should be minimum 7 character"

        user, created = User.objects.get_or_create(username=email, email=email)
        if created:
            user.password = make_password(password)
            user.save()

        res.status_code = 200
        res.success = True
        res.body = generate_user_obj(user)

        return res.json_response()

    def put(self, request):
        email = request.data.get("email", "")
        first_name = request.data.get("first_name", "")
        last_name = request.data.get("last_name", "")
        phone = request.data.get("phone", "")
        res = APIResponse()

        if not email:
            res.status_code = 400
            res.error = "email should not be empty"
        try:
            user = User.objects.get(Q(username=email) | Q(email=email))
            user.first_name = first_name
            user.last_name = last_name
            user.phone = phone
            user.save()
            res.status_code = 200
            res.success = True
            res.body = generate_user_obj(user)
        except User.DoesNotExist:
            res.status_code = 400
            res.error = "user with this email not exist "

        return res.json_response()


def generate_user_obj(obj):
    return {
        'id': obj.id,
        'first_name': obj.first_name,
        'last_name': obj.last_name,
        'username': obj.username,
        'email': obj.email,
        'phone': obj.phone,
        'user_type': obj.get_user_type_display()
    }
