from django.views import View
from django.shortcuts import render
from . import forms


class LoginView(View):
    def get(self, request):
        # form = forms.LoginForm()
        form = forms.LoginForm(initial={"email": "aaa@aaa.com"})  # test 때문에 기본 값 설정
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

        return render(request, "users/login.html", {"form": form})
