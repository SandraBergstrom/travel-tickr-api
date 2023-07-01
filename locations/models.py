from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=150, default="Unknown")

    def __str__(self):
        return f"{self.name}, {self.country}"