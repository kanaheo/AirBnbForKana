from django.db import models
from core import models as core_model

# Create your models here.


class List(core_model.AbstractTimeStampedModel):
    """List Model Definition"""

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return self.name
