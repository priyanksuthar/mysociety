from rest_framework import serializers
from event.models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ("id", "title", "details", "start_date", "end_date", "image",
                  "building", "committee")