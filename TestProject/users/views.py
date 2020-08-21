from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser

# Create your views here.

def register(request):
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CreateUser()
    return render(request, "users/register.html", {"form": form})
