from .login import login_view, logout_view, register
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', login_view, name='welcome'),
    url(r'^login/$', login_view, name='login',),
    url(r'^register/$', register,  name='register'),
    url(r'^logout/$', logout_view, name='logout'),
]
