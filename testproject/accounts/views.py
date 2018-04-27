from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import (
    RegisterationForm, 
    EditProfileForm
)
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# there are two type of views class based and function based

def registerUser(request):
    if request.method == "POST":
        form = RegisterationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/accounts/login")
    else:
        form = RegisterationForm()

        args = {"form": form}

        return render(request,"accounts/registration.html",args)

# @login_required
def profile(request, pk=None):
    # user = None
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    args = {'user':user}
    return render(request,"accounts/profile.html",args)


# @login_required
def editProfile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid:
            form.save()
            return redirect("/accounts/profile")
    
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request,"accounts/edit_profile.html",args)

# @login_required
def changePassword(request):
    if request.method=="POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("/accounts/profile")

    else:
            form = PasswordChangeForm(user=request.user)
            args = {'form':form}
            return render(request,"accounts/change_password.html",args)







