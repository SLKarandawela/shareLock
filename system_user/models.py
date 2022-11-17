from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_admin = models.BooleanField()
    is_manager = models.BooleanField()
    is_worker = models.BooleanField()


