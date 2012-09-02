from django.contrib import admin
from schoolreport.models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'school')


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'emis', 'physical_address', 'school_sector')
    ordering = ('name',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(School, SchoolAdmin)
