from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    image = models.ImageField(upload_to='profile_pics/', default='profile_pics/avatar.png')
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True)
    