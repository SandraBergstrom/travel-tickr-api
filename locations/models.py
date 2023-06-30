from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Location(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='location', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name