
from django.conf.urls import url, include
from django.contrib import admin

from sitetutorial import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',views.hello),
    url(r'^meta/$',views.display_meta),
    url(r'^time/$',views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$',views.future_datetime),
    url(r'^siteapp/',include('siteapp.urls',namespace="siteapp")),
    url(r'^books/',include('books.urls',namespace="books")), #try only '^'
]
