
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    twitter_token = models.CharField(max_length=255, blank=True, null=True)
    facebook_token = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
