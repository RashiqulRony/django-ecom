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

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.username = None

    @property
    def __str__(self):
        return self.username


class Customer(models.Model):
    user = models.OneToOneField(User, related_name="customer", on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    avatar = models.ImageField(null=True)
    address = models.ImageField(null=True, default=400)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.username = None

    @property
    def __str__(self):
        return self.username


