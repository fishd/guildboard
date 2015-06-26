from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from people.views import (
    edit_account,
    JoinGym,
    CreateGym,
    CreateFederation
)


urlpatterns = patterns(
    'people',
    url(
        r'^acct/$', 
        edit_account,
        name="acct_edit", 
    ),
    url(
        r'^create_gym/$', 
        CreateGym.as_view(),
        name="gym_create", 
    ),
    url(
        r'^join_gym/$',
        JoinGym.as_view(),
        name="join_gym"
    ),
    url(
        r'^create_fed/$', 
        CreateFederation.as_view(),
        name="fed_create",
    ),

)
