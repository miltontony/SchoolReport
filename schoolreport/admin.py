from django.contrib import admin
from schoolreport.models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'school')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(School)
admin.site.register(SchoolStatus)
admin.site.register(SchoolType)
admin.site.register(Municipality)
admin.site.register(District)