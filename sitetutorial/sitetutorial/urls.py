
from django.conf.urls import url, include
from django.contrib import admin

from sitetutorial import views
from sitetutorial import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',views.hello),
    url(r'^meta/$',views.display_meta),
    url(r'^time/$',views.current_datetime),
    url(r'^time/plus/(?P<fhours>\d{1,2})/$',views.future_datetime),

    url(r'^contact/',include([
        url(r'^$',views.contact),
        url(r'^thanks/$',views.contact),
    ])),

    
    url(r'^siteapp/',include('siteapp.urls',namespace="siteapp")),
    url(r'^books/',include('books.urls',namespace="books")), #try only '^'
]

if settings.DEBUG:
    urlpatterns+=[url(r'^debuginfo/$',views.debug)]
