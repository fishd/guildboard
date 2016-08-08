from django.conf.urls import url
from django.views.generic import TemplateView
from lifts.views import (
    MyEntryList,
    edit_an_entry,
    EntryDetail,
    CreateEntry
)


from lifts.record_views import GymRecords

RECORDS_PREFIX = "records"
urlpatterns = [
    url(
        r'^records/$',
        GymRecords.as_view(),
        name="records",
        prefix=RECORDS_PREFIX
    ),
]

LIFT_PREFIX = "lifts"
urlpatterns += [
    url(
        r'^manage$',
        MyEntryList.as_view(),
        name="lifts_manage",
        prefix=LIFT_PREFIX
    ),
    url(
        r'^create$',
        CreateEntry.as_view(),
        name="lifts_create",
        prefix=LIFT_PREFIX
    ),
    url(
        r'^edit$',
        MyEntryList.as_view(),
        name="lifts_edit",
        prefix=LIFT_PREFIX
    ),
    url(
        r'^edit/(?P<entry_id>\w+)$',
        edit_an_entry,
        name="lifts_edit_entry",
        prefix=LIFT_PREFIX
    ),
    url(
        r'^entries/(?P<id>\d+)$',
        EntryDetail.as_view(),
        name="lifts_entry_detail",
        prefix=LIFT_PREFIX
    ),
]
