from rest_framework import serializers
from resident.models import Buildings, Wings, Flats


class BuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buildings
        fields = ("id", "name", "address", "city", "state")


class WingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wings
        fields = ("id", "name", "building")


class FlatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flats
        fields = ("id", "number", "building", "user", "wing")
