from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(False)
    status = models.BooleanField(False)

