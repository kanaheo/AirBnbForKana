from django.views.generic import ListView, DetailView
from . import models


class HomeView(ListView):

    """HOmeView Definition"""

    model = models.Room
    paginate_by = 10
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """RoomDetail Definition"""

    model = models.Room


# 아래에 있는게 위에 한줄로 or 별로 안쓰는데 끝남 ;
# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         # 404는 raise !
#         raise Http404()
