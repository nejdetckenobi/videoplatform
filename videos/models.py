from django.contrib.auth.models import User
from django.db import models

from videos.storage import videostorage


class Video(models.Model):
    id = models.AutoField(primary_key=True)
    original_url = models.URLField()
    file = models.FileField(storage=videostorage, null=True, blank=True)
    status = models.BooleanField(default=None, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
