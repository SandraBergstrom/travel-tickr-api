from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Location(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=100, default="Unknown")

    def __str__(self):
        return self.name
