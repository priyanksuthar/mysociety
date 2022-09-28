from django.db import models
from user.models import User, CommonModel
# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, unique=True)
    status = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, unique=True)
    state = models.ForeignKey(State, blank=False, null=False,
                              related_name="state", on_delete=models.CASCADE)
    status = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.name}"


class Buildings(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    city = models.ForeignKey(City, related_name="buildings", on_delete=models.CASCADE)
    state = models.ForeignKey(State, related_name="buildings", on_delete=models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} | {self.name}"


class Wings(models.Model):
    name = models.CharField(max_length=2, null=False, blank=False)
    building = models.ForeignKey(Buildings, related_name="wings", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} | {self.building.name}"

    class Meta:
        unique_together = ("name", "building")


class Flats(CommonModel):
    number = models.IntegerField(null=False, blank=False)
    building = models.ForeignKey(Buildings, related_name="flats", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="flats", on_delete=models.CASCADE)
    wing = models.ForeignKey(Wings, related_name="flats", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} | {self.wing.name} | {self.building.name}"

    class Meta:
        unique_together = ("number", "building", "wing")
