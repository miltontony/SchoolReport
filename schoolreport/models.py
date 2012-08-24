from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User')
    school = models.TextField(default='')

class School(models.Model):
	emis = models.IntegerField(unique = True)
	province = models.CharField(default='', max_length=2, blank=True, null=True)
	school_status = models.CharField(default='', max_length=100, blank=True, null=True)
	name = models.CharField(default='', max_length=100, blank=True, null=True)
	school_type = models.CharField(default='', max_length=100, blank=True, null=True)
	school_sector = models.CharField(default='', max_length=100, blank=True, null=True)
	specialisation = models.CharField(default='', max_length=100, blank=True, null=True)
	section21 = models.BooleanField()
	fee = models.IntegerField()
	municipality = models.CharField(default='', max_length=100, blank=True, null=True)
	telephone = models.CharField(default='', max_length = 30, blank=True, null=True)
	longitude = models.CharField(default='', max_length=20, blank=True, null=True)
	latitude = models.CharField(default='', max_length=20, blank=True, null=True)
	language = models.CharField(default='', max_length = 20, blank=True, null=True)
	principal = models.CharField(default='', max_length = 30, blank=True, null=True)
	physical_address = models.CharField(default='', max_length = 255, blank=True, null=True)
	district = models.CharField(max_length=100, blank=True, null=True)
	circuit = models.IntegerField(blank=True, null=True)
	students = models.IntegerField(blank=True, null=True)
	teachers = models.IntegerField(blank=True, null=True)
	passrate_2009 = models.IntegerField(blank=True, null=True)
	passrate_2010 = models.IntegerField(blank=True, null=True)
	passrate_2011 = models.IntegerField(blank=True, null=True)

def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_profile, sender=User,
                  dispatch_uid="users-profilecreation-signal")
