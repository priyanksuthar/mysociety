from committee.models import Committees, CommitteeRoles, CommitteeMembers
from rest_framework import serializers


class CommitteeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Committees
        fields = ("id", "name", "building")


class CommitteeRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommitteeRoles
        fields = ("id", "name", "building")


class CommitteeMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommitteeMembers
        fields = ("id", "user", "role", "committee")

