from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    role = models.CharField(max_length=20, default=None, null=True, blank=True)

    def __str__(self):
        return (self.first_name + " " + self.last_name).strip()


