from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'login.login.login_view', name="login"),
    url(r'^register/$', 'login.login.register',  name='register'),
    url(r'^login/$', 'login.login.login_view', name='login-specific',),
    url(r'^logout/$', 'login.login.logout_view', name='logout'),
    url(r'^home/$', 'views.main', name="main"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url('^lifts/', include('lifts.urls')),
    url('^people/', include('people.urls')),
    url('^records/', include('records.urls'))
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
