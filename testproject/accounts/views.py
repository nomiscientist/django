from django.shortcuts import render, HttpResponse

# Create your views here.
# there are two type of views class based and function based

def home(request):
    # return  HttpResponse("Hello Pakistan from Home page of accounts!!")

    # numbers = [1,2,3,4,5]

    # name = "mfaisal"
    # args = {"name":name,"numbers":numbers}

    return render(request, 'accounts/home.html')


