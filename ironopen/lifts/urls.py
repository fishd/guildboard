from django.conf.urls import url
from django.views.generic import TemplateView
from lifts.feed_views import (
    GymEntryList,
    FederationEntryList,
    PublicEntryList,
)
from lifts.entry_views import (
    MyEntryList,
    edit_an_entry,
    EntryDetail,
    CreateEntry
)


LIFT_PREFIX = "lifts"
urlpatterns = [
    # url(
    #     r'^feed$',
    #     GymEntryList.as_view(),
    #     name="lifts",
    #     prefix=LIFT_PREFIX
    # ),
    # url(
    #     r'^feed/gym/$',
    #     GymEntryList.as_view(),
    #     name="lifts_feed_gym",
    #     prefix=LIFT_PREFIX
    # ),
    # url(
    #     r'^feed/federation/$',
    #     FederationEntryList.as_view(),
    #     name="lifts_feed_fed",
    #     prefix=LIFT_PREFIX
    # ),
    # url(
    #     r'^feed/all/$',
    #     PublicEntryList.as_view(),
    #     name="lifts_feed_pub",
    #     prefix=LIFT_PREFIX
    # ),

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
