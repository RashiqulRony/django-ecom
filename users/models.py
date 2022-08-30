from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Vendor(models.Model):
    user = models.OneToOneField(User, related_name="vendor", on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    avatar = models.ImageField(null=True)
    address = models.CharField(null=True, max_length=400)


class Customer(models.Model):
    user = models.OneToOneField(User, related_name="customer", on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    avatar = models.ImageField(null=True)
    address = models.CharField(null=True, max_length=400)
