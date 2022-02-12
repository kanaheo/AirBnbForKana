from django.urls import path
from rooms import views as room_views

app_name = "core"


urlpatterns = [path("", room_views.IndexView.as_view(), name="home")]
