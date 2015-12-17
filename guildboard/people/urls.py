from django.conf.urls import url
from django.views.generic import TemplateView
from people.views import (
    edit_account,
    JoinGym,
    CreateGym,
    CreateFederation
)


PEOPLE_PREFIX = "people"
urlpatterns = [
    url(
        r'^acct/$',
        edit_account,
        name="acct_edit",
        prefix=PEOPLE_PREFIX
    ),
    url(
        r'^create_gym/$',
        CreateGym.as_view(),
        name="gym_create",
        prefix=PEOPLE_PREFIX
    ),
    url(
        r'^join_gym/$',
        JoinGym.as_view(),
        name="join_gym",
        prefix=PEOPLE_PREFIX
    ),
    url(
        r'^create_fed/$',
        CreateFederation.as_view(),
        name="fed_create",
        prefix=PEOPLE_PREFIX
    ),
]
