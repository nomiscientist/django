from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm

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
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/account/login")
    else:
        form = UserCreationForm()

        args = {"form": form}

        return render(request,"accounts/registration.html",args)
