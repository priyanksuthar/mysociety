from django.db import models
from user.models import CommonModel, User
from resident.models import Buildings
from committee.models import Committees
# Create your models here.


def event_image_dir(instance, filename):
    return 'event_image/{0}/{1}'.format(instance.building.id, filename)


class Event(CommonModel):
    title = models.CharField(max_length=500, blank=False, null=False)
    details = models.TextField(blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    image = models.ImageField(upload_to=event_image_dir, blank=True, null=True, max_length=500)
    building = models.ForeignKey(Buildings, related_name="event", on_delete=models.CASCADE)
    committee = models.ForeignKey(Committees, related_name="event", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} | {self.building.name}"


class EventStatus(models.Model):
    SENT = 1
    UNREAD = 2
    READ = 3
    NOT_SENT = 4
    STATUS = [
        ("Sent", SENT),
        ("Unread", UNREAD),
        ("Read", READ),
        ("NotSent", NOT_SENT)
    ]
    user = models.ForeignKey(User, related_name="event_status", on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="event_status", on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=4)

    def __str__(self):
        return f"{self.id} | {self.event.title}"
