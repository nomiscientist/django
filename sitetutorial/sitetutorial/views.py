from django.shortcuts import render
from django.http import HttpResponse, Http404

import datetime

def hello(request):
    return HttpResponse("Hello Pakistan!")

def current_datetime(request):
    return HttpResponse("It is now: %s" % datetime.datetime.now())

def future_datetime(request, fhours):
    try:
        fhours = int(fhours)
    except ValueError:
        raise Http404()

    ftime = datetime.datetime.now() + datetime.timedelta(hours=fhours)
    return HttpResponse("Future Hour(s): %s Gets us: %s"%(fhours,ftime))
    