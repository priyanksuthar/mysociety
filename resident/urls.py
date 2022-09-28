from django.urls import path
from resident.views import *

urlpatterns = [
    path('building/', BuildingsAPI.as_view()),
    path('building/<str:building_id>/', BuildingsAPI.as_view()),
    path('wing/', WingsAPI.as_view()),
    path('wing/<str:wing_id>/', WingsAPI.as_view()),
    path('flat/', FlatAPI.as_view()),
    path('flat/<str:flat_id>/', FlatAPI.as_view()),
]