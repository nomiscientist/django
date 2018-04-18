from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse

import re

EXEMPT_URL = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings,'LOGIN_EXEMPT_URLS'):
    EXEMPT_URL+=[re.compile(url) for url in settings.LOGIN_EXEMPT_URLS ]

class LoginRequiredMiddleware():
    def __init__(self,get_response):
        self.get_response = get_response

    
    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_view(self,request,view_func, view_args, view_kwargs):
        assert hasattr(request,'user')

        path = request.path_info.lstrip('/')
        print(path)

        # if not request.user.is_authenticated():
        #     if not any(url.match(path) for url in EXEMPT_URL):
        #         return redirect(settings.LOGIN_URL)

        if path == reverse("accounts:logout").lstrip('/'):
            logout(request)


        exempt_url = any(url.match(path) for url in EXEMPT_URL)

        if request.user.is_authenticated() and exempt_url:
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif request.user.is_authenticated() or exempt_url:
            return None
        else:
            return redirect(settings.LOGIN_URL)

