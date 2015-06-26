from django.conf.urls import patterns, url

from .views import GymRecords
urlpatterns = patterns(
    'records',
    url(
        r'^records/gym$', 
        GymRecords.as_view(),
        name="records", 
    ),
)
