from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from jmbocomments.models import UserComment


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User')
    school = models.TextField(default='')

REPORT_CATEGORY_CHOICES = (
        (0, 'Maintenance'),
        (1, 'Abuse'),
        (2, 'Textbooks'),
        (3, 'Crime'),
        (4, 'Bullying'),
        )


class UserReport(UserComment):
    category = models.PositiveIntegerField(choices=REPORT_CATEGORY_CHOICES,
                                            null=False, blank=False, default=0)

def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_profile, sender=User,
                  dispatch_uid="users-profilecreation-signal")
