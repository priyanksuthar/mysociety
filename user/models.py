from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


def profile_pic_dir(instance, filename):
    return 'profile_pic/{0}/{1}'.format(instance.username, filename)


class User(AbstractUser):
    SECRETARY = 1
    CHAIRMAN = 2
    TREASURER = 3
    OWNER = 4
    MEMBER = 5
    TYPES = (
        (SECRETARY, "Secretary"),
        (CHAIRMAN, "Chairman"),
        (TREASURER, "Treasurer"),
        (OWNER, "Owner"),
        (MEMBER, "Member")
    )
    email = models.EmailField(max_length=150, blank=False, null=False, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    picture = models.ImageField(upload_to=profile_pic_dir, blank=True, null=True, max_length=500)
    user_type = models.IntegerField(choices=TYPES, default=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}"


class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, related_name='%(class)s_createdby', on_delete=models.CASCADE)
    modified_by = models.ForeignKey(
        User, related_name='%(class)s_modifiedby', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True
