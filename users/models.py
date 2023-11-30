from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profile")
    bio = models.TextField(null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user)
