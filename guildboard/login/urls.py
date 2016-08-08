from .login import EmailRegistration, login_view, register, logout_view, activate_acct, resend_activation_view
from django.conf.urls import url, include


urlpatterns = [
    url(r'^email/$', EmailRegistration.as_view(), name="email_registration"),
    url(r'^activate/(.*)$', activate_acct, name="activate_acct"),
    url(r'^resend/(.*)$', resend_activation_view, name="resend_activation"),
    url(r'^login/$', login_view, name='login',),
    url(r'^register/$', register,  name='register'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^reset/', include('password_reset.urls'))
]
