from django.conf.urls import url
from siteapp import views

urlpatterns = [
    url(r'^order/$',views.order),
    url(r'^test/$',views.test),    

]