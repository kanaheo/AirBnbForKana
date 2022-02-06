from django.db import models
from django.utils import timezone
from core import models as core_models
from django import template


class Reservation(core_models.AbstractTimeStampedModel):

    """Reservation Model Definition"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "pending"),
        (STATUS_CONFIRMED, "confirmed"),
        (STATUS_CANCELED, "canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        now = timezone.localdate()
        return now >= self.check_in and now <= self.check_out

    in_progress.boolean = True  # boolean형태로 바꿔주기

    register = template.Library()

    @register.filter
    def is_finished(self):
        now = timezone.localdate()
        return now > self.check_out

    is_finished.boolean = True  # boolean형태로 바꿔주기
