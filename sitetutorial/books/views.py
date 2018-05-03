from django.shortcuts import render
from django.http import HttpResponse
from books import models

# Create your views here.

# def search_form(request):
#     return render(request,"books/search_form.html")


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            print(q)
            error = True
        else:
            book_obj = models.Book.objects.filter(title__icontains=q)
            args = {'books':book_obj,'query':q}
            return render(request,"books/search_results.html",args)
            # q = "Please submit a search term."
            # return HttpResponse(q)
    return render(request,"books/search_form.html",{"error":error})



    
    
    
