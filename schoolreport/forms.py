from django.contrib.auth.forms import UserCreationForm
from django.forms import *


class MobiUserCreationForm(UserCreationForm):
    school = CharField(required=True)
    username = RegexField(
        label='Phone number',
        regex=r'^[0-9]+$',
        help_text='Required. Valid phone number in the format: 0821234567',
        error_message='Please enter a valid phone number without spaces. e.g 0821234567')
