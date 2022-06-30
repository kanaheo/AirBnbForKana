from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.log_out, name="logout"),  # 함수는 그냥
    path("signup", views.SignUpView.as_view(), name="signup"),  # class 는 as_view
    path("verify/<str:key>", views.complete_verification, name="complete-verification"),
    # MUST 아래처럼 쓰고 싶다면 views log_out함수가 클래스 밖에 있어야함 !
    # path("logout", views.log_out, name="logout"),
    # MUST 아래처럼 쓰고 싶다면 views log_out함수가 클래스 안에 있어야함 !
    # path("logout", views.LoginView.log_out, name="logout"),
]
