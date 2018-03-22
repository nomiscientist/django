from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    city = models.CharField(max_length=50,default='')
    phone = models.IntegerField(default=0)