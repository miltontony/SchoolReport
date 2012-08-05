from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User')
    school = models.TextField(default='')

class SchoolStatus(models.Model):
	name = models.CharField(max_length = 10)

class SchoolType(models.Model):
	name = models.CharField(max_length = 20)

class Municipality(models.Model):
	name = models.CharField(max_length = 100)

class District(models.Model):
	name = models.CharField(max_length = 100)

class School(models.Model):
	emis = models.IntegerField(unique = True)
	school_status = models.OneToOneField(SchoolStatus)
	name = models.CharField(max_length=100)
	school_type = models.OneToOneField(SchoolType)
	section21 = models.BooleanField()
	fee = models.IntegerField()
	municipality = models.OneToOneField(Municipality)
	telephone = models.CharField(max_length = 30)
	longitude = models.DecimalField(max_digits=10, decimal_places=7)
	latitude = models.DecimalField(max_digits=10, decimal_places=7)
	language = models.CharField(max_length = 20)
	principal = models.CharField(max_length = 30)
	physical_address = models.CharField(max_length = 255)
	district = models.OneToOneField(District)

def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_profile, sender=User,
                  dispatch_uid="users-profilecreation-signal")
