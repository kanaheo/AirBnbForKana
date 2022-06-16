from django.views.generic import ListView
from . import models


class HomeView(ListView):

    """HOmeView Definition"""

    model = models.Room
    paginate_by = 10
    ordering = "created"
    context_object_name = "rooms"
