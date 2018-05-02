from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template.loader import get_template

import datetime

def hello(request):
    return HttpResponse("Hello Pakistan!")

# Old ways of rendering
# def current_datetime(request):
#     now = datetime.datetime.now()
#     t = get_template("current_datetime.html")
#     c = {'current_date': now}
#     html = t.render(c)
#     return HttpResponse(html)

# New way render ways
def current_datetime(request):
    now = datetime.datetime.now()
    args = {'current_date': now}
    return render(request,"current_datetime.html",args)

def future_datetime(request, fhours):
    try:
        fhours = int(fhours)
    except ValueError:
        raise Http404()

    ftime = datetime.datetime.now() + datetime.timedelta(hours=fhours)
    args = {'hour_offset': fhours,"next_time":ftime}
    return render(request,"future_datetime.html",args)
    