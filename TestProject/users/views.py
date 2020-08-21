from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CreateUser, UpdateProfile, UpdateAdminProfile, UpdateUserPermissions


# Create your views here.

def register(request):
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully")
            return redirect("home")
    else:
        form = CreateUser()
    return render(request, "users/register.html", {"form": form})


def profile(request):
    if request.user.is_authenticated:
        # user = request.user
        users = None
        if request.user.is_superuser == True:
            users = User.objects.all()
        return render(request, "users/profile.html", {"users": users})
    else:
        return redirect("login")


@login_required()
def profile_update(request):
    if request.method == "POST":
        user = request.user
        if request.user.is_superuser == True:
            form = UpdateAdminProfile(request.POST, instance=user)
        else:
            form = UpdateProfile(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        if request.user.is_superuser == True:
            form = UpdateAdminProfile(instance=request.user)
        else:
            form = UpdateProfile(instance=request.user)
    return render(request, "users/user_update.html", {"form": form})


def user_detail(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(pk=id)
        if request.method == "POST":
            form = UpdateUserPermissions(request.POST, instance=user)
            if form.is_valid():
                form.save()
        else:
            form = UpdateUserPermissions(instance=user)
    return render(request, "users/user_details.html", {"user": user, "form": form})
