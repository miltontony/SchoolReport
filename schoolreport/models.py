from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User')
    school = models.TextField(default='')


def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_profile, sender=User,
                  dispatch_uid="users-profilecreation-signal")
