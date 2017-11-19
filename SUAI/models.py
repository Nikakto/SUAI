from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=30)
    removed = models.BooleanField(default=False)
    source = models.ImageField()
    

class News(models.Model):
    content = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    removed = models.BooleanField(default=False)
    title = models.CharField(max_length=30)