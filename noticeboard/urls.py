from django.urls import path
from noticeboard.views import NoticeStatusAPI, NoticeBoardAPI

urlpatterns = [
    path('noticeboard/', NoticeBoardAPI.as_view()),
    path('noticeboard/<str:notice_id>/', NoticeBoardAPI.as_view()),
    path('notice-status/', NoticeStatusAPI.as_view()),
    path('notice-status/<str:status_id>/', NoticeStatusAPI.as_view())
]