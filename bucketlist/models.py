from django.contrib.auth.models import User
from django.db import models


class BucketListItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} by {self.owner}'
