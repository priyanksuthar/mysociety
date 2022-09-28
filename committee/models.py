from django.db import models
from user.models import CommonModel, User
from resident.models import Buildings
# Create your models here.


class Committees(CommonModel):
    name = models.CharField(max_length=400, blank=False, null=False)
    building = models.ForeignKey(Buildings, related_name="committees", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.building.name}"

    class Meta:
        unique_together = ("name", "building")


class CommitteeRoles(CommonModel):
    name = models.CharField(max_length=400, blank=False, null=False)
    building = models.ForeignKey(Buildings, related_name="committee_roles", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} |  {self.building}"

    class Meta:
        unique_together = ("name", "building")


class CommitteeMembers(CommonModel):
    user = models.ForeignKey(User, related_name="committee_members", on_delete=models.CASCADE)
    role = models.ForeignKey(CommitteeRoles, related_name="committee_members", on_delete=models.CASCADE)
    committee = models.ForeignKey(Committees, related_name="committee_members", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} | {self.user.name}"

    class Meta:
        unique_together = ("user", "committee")

