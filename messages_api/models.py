from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel


# Create your models here.


class Message(TimeStampedModel):
    subject = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    is_active = models.BooleanField(default=1)
    send_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.subject


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.FileField(upload_to='post_images')
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.title