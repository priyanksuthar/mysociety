from django.urls import path
from committee.views import *

urlpatterns = [
    path('committee/', CommitteeAPI.as_view()),
    path('committee/<str:committee_id>/', CommitteeAPI.as_view()),
    path('committee-role/', CommitteeRoleAPI.as_view()),
    path('committee-role/<str:role_id>/', CommitteeRoleAPI.as_view()),
    path('committee-member/', CommitteeMemberAPI.as_view()),
    path('committee-member/<str:member_id>/', CommitteeMemberAPI.as_view()),
]