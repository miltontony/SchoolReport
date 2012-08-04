from django.db import models


class UserProfile(models.Model):
    school = models.TextField(default='')
