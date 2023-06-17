from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Post(models.Model):
    """
    Represents a post made by the user
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     if self.image:
    #         img = Image.open(self.image.path)
    #         max_size = (1024, 1024)
    #         img.thumbnail(max_size, Image.ANTIALIAS)

    #         # Adjust the image quality to balance size and visual quality
    #         img.save(self.image.path, optimize=True, quality=90)

