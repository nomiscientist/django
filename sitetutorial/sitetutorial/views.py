from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from sitetutorial import forms

import datetime
from django.core.mail import send_mail, get_connection


def contact(request):
    thanks_message = ""
    if request.path == "/contact/thanks/":
        thanks_message = "Thanks for your feedback"


    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd['email'],
                ['imfaisalpk@gmail.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = forms.ContactForm(
            initial = {'subject': "I love your site!"}
        )
    
    return render(request,"contact_form.html",{"form":form, "message":thanks_message})

def debug(request):
    pass


def hello(request):
    return HttpResponse("Hello Pakistan!")


def display_meta(request):
    # try:
    #     ua = request.META['HTTP_USER_AGENT']
    # except KeyError:
    #     ua = 'unknown'

    # ua = request.META.get("HTTP_USER_AGENT","unknown")
    # return HttpResponse("Your Browser Info: %s" % ua )

    values = request.META
    html = []
    for key in sorted(values):
        html.append("<tr><td>%s</td><td>%s</td></tr>"%(key,values[key]))
    return HttpResponse("<table>%s</table>"%"\n".join(html))


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

def future_datetime(request, fhours=1):
    try:
        fhours = int(fhours)
    except ValueError:
        raise Http404()

    ftime = datetime.datetime.now() + datetime.timedelta(hours=fhours)
    args = {'hour_offset': fhours,"next_time":ftime}
    return render(request,"future_datetime.html",args)
    