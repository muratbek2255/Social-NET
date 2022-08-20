from django.conf import settings
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from comments.models import AbstractComment


class Post(models.Model):
    title = models.CharField(max_length=155, default='Cool news')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    moderat = models.BooleanField(default=True)
    views_count = models.PositiveIntegerField(default=0)
    customuser = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f'id:{self.id} and user: {self.customuser}'

    def comments_count(self):
        return self.comments.count()


class Comment(AbstractComment, MPTTModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    parent = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return "{} - {}".format(self.user, self.post)
