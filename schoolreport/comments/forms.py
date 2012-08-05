from jmbocomments.forms import UserCommentForm
from schoolreport.comments.models import REPORT_CATEGORY_CHOICES
from django.forms import *


class UserReportForm(UserCommentForm):
    category = IntegerField(required=False,\
                widget=RadioSelect(choices=REPORT_CATEGORY_CHOICES))
