from django.shortcuts import render
from django.http import HttpResponse
from books import models

# Create your views here.

# def search_form(request):
#     return render(request,"books/search_form.html")


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append("Please submit search term.")
        elif len(q) >= 20:
            errors.append("Please submit a search term 20 characters or shorter.")
        else:
            book_obj = models.Book.objects.filter(title__icontains=q)
            args = {'books':book_obj,'query':q}
            return render(request,"books/search_results.html",args)
            # q = "Please submit a search term."
            # return HttpResponse(q)
    return render(request,"books/search_form.html",{"errors":errors})



    
    
    
