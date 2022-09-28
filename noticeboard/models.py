from django.db import models
from user.models import User, CommonModel
from resident.models import Buildings
# Create your models here.


def notice_image_dir(instance, filename):
    return 'notice_image/{0}/{1}'.format(instance.building.id, filename)


class NoticeBoard(CommonModel):
    title = models.CharField(max_length=500, blank=False, null=False)
    notice = models.TextField(blank=False, null=False)
    notice_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to=notice_image_dir, blank=True, null=True, max_length=500)
    building = models.ForeignKey(Buildings, related_name="notice", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class NoticeStatus(models.Model):
    SENT = 1
    UNREAD = 2
    READ = 3
    NOT_SENT = 4
    STATUS = [
        (SENT, "Sent"),
        (UNREAD, "Unread"),
        (READ, "Read"),
        (NOT_SENT, "Not Sent")
    ]
    user = models.ForeignKey(User, related_name="notice_status", on_delete=models.CASCADE)
    notice = models.ForeignKey(NoticeBoard, related_name="notice_status", on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=4)

    def __str__(self):
        return f"{self.id} | {self.notice.title}"

    class Meta:
        unique_together = ("notice", "user")

