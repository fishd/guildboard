from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from lifts.feed_views import (
    GymEntryList,
    FederationEntryList,
    PublicEntryList,
)
from lifts.entry_views import (
    MyEntryList,
    EntryDetail,
    CreateEntry
)


urlpatterns = patterns(
    'lifts',
    url(
        r'^feed$', GymEntryList.as_view(),
        name="lifts"
    ),
    url(
        r'^feed/gym/$', GymEntryList.as_view(),
        name="lifts_feed_gym"
    ),
    # url(
    #     r'^feed/federation/$', FederationEntryList.as_view(),
    #     name="lifts_feed_fed"
    # ),
    url(
        r'^feed/all/$', PublicEntryList.as_view(),
        name="lifts_feed_pub"
    ),

    url(
        r'^manage$', MyEntryList.as_view(),
        name="lifts_manage"
    ),
    url(
        r'^create$', CreateEntry.as_view(),
        name="lifts_create"
    ),
    url(
        r'^edit$', MyEntryList.as_view(),
        name="lifts_edit"
    ),
    url(
        r'^edit/(?P<entry_id>\w+)$', "entry_views.edit_an_entry",
        name="lifts_edit_entry"
    ),
    url(
        r'^entries/(?P<id>\d+)$', EntryDetail.as_view(),
        name="lifts_entry_detail"
    ),

)
