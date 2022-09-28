from rest_framework import serializers
from noticeboard.models import NoticeBoard, NoticeStatus


class NoticeBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoticeBoard
        fields = ("id", "title", "notice", "notice_date",
                  "image", "building", "created_by")


class NoticeStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoticeStatus
        fields = ("id", "user", "notice", "status")

