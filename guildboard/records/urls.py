from django.conf.urls import url

from .views import GymRecords

RECORDS_PREFIX = "records"
urlpatterns = [
    url(
        r'^records/gym$',
        GymRecords.as_view(),
        name="records",
        prefix=RECORDS_PREFIX
    ),
]
