from django.contrib import admin
from schoolreport.models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'school')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(School)