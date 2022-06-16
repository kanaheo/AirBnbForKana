from math import ceil
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = (
        models.Room.objects.all()
    )  # 여기서 불러 올 때는 그냥 선언만 ! 아직 디비에서 안가지고옴 ! 근데 저게 선언되면 디비를 불러옴
    paginator = Paginator(room_list, 10)
    try:
        rooms = paginator.page(int(page))
        return render(
            request,
            "rooms/home.html",
            context={"page": rooms},
        )
    # except EmptyPage:
    except Exception:   # 모든 에러
        rooms = paginator.page(1)
        return redirect("/")
