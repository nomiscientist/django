from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    city = models.CharField(max_length=50,default='')
    phone = models.IntegerField(default=0)

def createProfile(sender, **kwargs):
    if kwargs["created"]:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


signals.post_save.connect(createProfile,sender=User)