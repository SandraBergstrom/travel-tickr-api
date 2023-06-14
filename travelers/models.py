from django.db import models
from django.contrib.auth.models import User


class Traveler(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=500, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_uwgpte'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Travel Tickr: {self.owner}"
