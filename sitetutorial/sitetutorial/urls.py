
from django.conf.urls import url
from django.contrib import admin

from sitetutorial import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',views.hello),
    url(r'^time/$',views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$',views.future_datetime),
]
