from django.conf.urls import include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from login import login

admin.autodiscover()


urlpatterns = [
    url(r'^$', login.login_view, name="login"),
    url(r'^register/$', login.register,  name='register'),
    url(r'^login/$', login.login_view, name='login-specific',),
    url(r'^logout/$', login.logout_view, name='logout'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url('^lifts/', include('lifts.urls')),
    url('^people/', include('people.urls')),
    url('^records/', include('records.urls')),
]

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
