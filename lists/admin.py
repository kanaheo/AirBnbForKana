from django.contrib import admin
from . import models


@admin.register(models.Lists)
class ListAdmin(admin.ModelAdmin):

    """List Admin Definition"""

    pass
