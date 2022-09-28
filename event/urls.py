from django.urls import path
from event.views import EventAPI

urlpatterns = [
    path('event/', EventAPI.as_view()),
    path('event/<str:event_id>/', EventAPI.as_view()),
    path('event/', EventAPI.as_view()),
    path('event/<str:event_id>/', EventAPI.as_view())
]