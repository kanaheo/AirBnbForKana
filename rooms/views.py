from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
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


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    instant = request.GET.get("instant", False)
    super_host = request.GET.get("super_host", False)
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")

    # parameter에서 받아오는 것
    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "instant": instant,
        "super_host": super_host,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    # 모델(db)에서 받아오는 것
    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    return render(
        request,
        "rooms/search.html",
        {**form, **choices},
    )
