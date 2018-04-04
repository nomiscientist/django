from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)

urlpatterns =[
    url(r'^$',views.home),
    url(r'^home/$',views.home),
    url(r'^login/$',login,{'template_name':'accounts/login.html'}),
    url(r'^logout/$',logout,{'template_name':'accounts/logout.html'}),
    url(r'^register/$',views.registerUser, name="registerUser" ), 
    url(r'^profile/$',views.profile, name="profile" ),
    url(r'^profile/edit/$',views.editProfile, name="editProfile" ),
    url(r'^profile/change-password/$',views.changePassword, name="changePassword" ),
    url(r'^reset-password/$',password_reset,name="password_reset"),
    url(r'^reset-password/done/$',password_reset_done,name="password_reset_done"),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    password_reset_confirm,name="password_reset_confirm"),
    # python -m smtpd -n -c DebuggingServer localhost:1025
    url(r'^reset-password/complete/$',password_reset_complete,name="password_reset_complete")            
    
]