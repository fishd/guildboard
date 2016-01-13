from django.conf.urls import url

from .views import Leaderboard

RECORDS_PREFIX = "records"
urlpatterns = [
    url(
        r'^leaderboard/$',
        Leaderboard.as_view(),
        name="records",
        prefix=RECORDS_PREFIX
    ),

    # url(
    #     r'^records/(?P<filter>\w+)/$',
    #     GymRecords.as_view(),
    #     name="records",
    #     prefix=RECORDS_PREFIX
    # ),
]
