from django.shortcuts import render
from . import models

# django는 유저가 처음에 이 페이지로 왔을 때 모든 정보를 request를 해서 준다 !
# 로그인을 햇는지, 이 페이지에 들왓는지를 request를 통해서 첫번째 인자로 다 줌 ! 개쩜
# 그리고 항상 반환해야함 ! httpResponse를 반환해야함 !
# 우린 HttpResponse안에다 매번 이렇게 안에다가 <div>hello</div> 이런식으로 안하고 render을 쓸거다
def all_rooms(request):  # <- 여기 이름은 core url부분에서 이름이 같아야!
    all_rooms = models.Room.objects.all()

    return render(request, "rooms/index.html", context={"rooms": all_rooms})
