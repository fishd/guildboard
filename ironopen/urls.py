from django.conf.urls import include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import views

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomePageView.as_view(), name="home"),
    url('^auth/', include('login.urls')),
    url(r'^people/', include('people.urls')),
    url(r'^records/', include('records.urls')),
]

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
