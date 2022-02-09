from math import ceil
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models

# django는 유저가 처음에 이 페이지로 왔을 때 모든 정보를 request를 해서 준다 !
# 로그인을 햇는지, 이 페이지에 들왓는지를 request를 통해서 첫번째 인자로 다 줌 ! 개쩜
# 그리고 항상 반환해야함 ! httpResponse를 반환해야함 !
# 우린 HttpResponse안에다 매번 이렇게 안에다가 <div>hello</div> 이런식으로 안하고 render을 쓸거다
def all_rooms(request):  # <- 여기 이름은 core url부분에서 이름이 같아야!
    page = request.GET.get("page", 1)
    room_list = (
        models.Room.objects.all()
    )  # 여기서는 처음에 query set만 불러오기만 할 뿐 이걸 밑에서 쓰면 서버에 부담이!
    # paginator = Paginator(room_list, 10, orphans=5)  # 오브젝트목록, 페이지 수
    paginator = Paginator(room_list, 10, orphans=5)  # 오브젝트목록, 페이지 수
    try:
        rooms = paginator.page(int(page))
        return render(
            request,
            "rooms/index.html",
            context={"page": rooms},
        )
    except EmptyPage:
        return redirect("/")
