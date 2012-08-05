from schoolreport.comments.models import UserReport
from schoolreport.comments.forms import UserReportForm


def get_model():
    return UserReport


def get_form():
    return UserReportForm
