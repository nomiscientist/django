from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import (
    RegisterationForm, 
    EditProfileForm
)
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.
# there are two type of views class based and function based

def home(request):
    # return  HttpResponse("Hello Pakistan from Home page of accounts!!")

    # numbers = [1,2,3,4,5]

    # name = "mfaisal"
    # args = {"name":name,"numbers":numbers}

    return render(request, 'accounts/home.html')

def registerUser(request):
    if request.method == "POST":
        form = RegisterationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/account/login")
    else:
        form = RegisterationForm()

        args = {"form": form}

        return render(request,"accounts/registration.html",args)


def profile(request):
    args = {'user':request.user}
    return render(request,"accounts/profile.html",args)



def editProfile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid:
            form.save()
            return redirect("/account/profile")
    
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request,"accounts/edit_profile.html",args)


def changePassword(request):
    if request.method=="POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("/account/profile")

    else:
            form = PasswordChangeForm(user=request.user)
            args = {'form':form}
            return render(request,"accounts/change_password.html",args)







