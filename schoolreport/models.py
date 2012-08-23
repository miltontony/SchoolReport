from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User')
    school = models.TextField(default='')

class School(models.Model):
	emis = models.IntegerField(unique = True)
	province = models.CharField(max_length=2)
	school_status = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	school_type = models.CharField(max_length=100)
	school_sector = models.CharField(max_length=100)
	specialisation = models.CharField(max_length=100)
	section21 = models.BooleanField()
	fee = models.IntegerField()
	municipality = models.CharField(max_length=100)
	telephone = models.CharField(max_length = 30)
	longitude = models.CharField(max_length=20)
	latitude = models.CharField(max_length=20)
	language = models.CharField(max_length = 20)
	principal = models.CharField(max_length = 30)
	physical_address = models.CharField(max_length = 255)
	district = models.CharField(max_length=100)
	circuit = models.IntegerField()
	students = models.IntegerField()
	teachers = models.IntegerField()
	passrate_2009 = models.IntegerField()
	passrate_2010 = models.IntegerField()
	passrate_2011 = models.IntegerField()

def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_profile, sender=User,
                  dispatch_uid="users-profilecreation-signal")
