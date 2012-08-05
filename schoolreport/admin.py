from django.contrib import admin
from schoolreport.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'school')

admin.site.register(UserProfile, UserProfileAdmin)
