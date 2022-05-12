from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField()
    updated = models.DateTimeField()
