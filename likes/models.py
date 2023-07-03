from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from comments.models import Comment


class Like(models.Model):
    """
    Like model with a foreign key to user
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(Comment, related_name='comments', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        # unique_together = ['owner', 'post']

    def __str__(self):
        if self.post:
            return f'{self.owner} {self.post}'
        else:
            return f'{self.owner} {self.comment}'
