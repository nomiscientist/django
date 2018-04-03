from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns =[
    url(r'^$',views.home),
    url(r'^home/$',views.home),
    url(r'^login/$',login,{'template_name':'accounts/login.html'}),
    url(r'^logout/$',logout,{'template_name':'accounts/logout.html'}),
    url(r'^register/$',views.registerUser, name="registerUser" ), 
    url(r'^profile/$',views.profile, name="profile" ),
    url(r'^profile/edit/$',views.editProfile, name="editProfile" ),
    url(r'^profile/change-password/$',views.changePassword, name="changePassword" )
    
]