from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import User


# Create your views here.

def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        re_password = request.POST["re-password"]

        user = User(
            username=username,
            password=make_password(password)
        )

        user.save()

        return render(request, "register.html")
