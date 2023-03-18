from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
    phone_number = models.PositiveIntegerField(null=True, blank=True)

    # def __str__(self):
    #     return self.name
