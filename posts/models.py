from django.db import models
from django.conf import settings  # for point to the cutomized name & phone of the user


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100, null=True)
    # author will ne show with an integer value for ex: the super user account author will be shown as #1 and so on
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.author
