from django.db import models
from jmbocomments.models import UserComment

REPORT_CATEGORY_CHOICES = (
        (0, 'Maintenance'),
        (1, 'Abuse'),
        (2, 'Textbooks'),
        (3, 'Crime'),
        (4, 'Bullying'),
        )


class UserReport(UserComment):
    category = models.PositiveIntegerField(choices=REPORT_CATEGORY_CHOICES,
                                            null=False, blank=False, default=0)
