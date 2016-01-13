from django.conf.urls import url
from django.views.generic import TemplateView
from people.views import (
    edit_account,
)


PEOPLE_PREFIX = "people"
urlpatterns = [
    url(
        r'^acct/$',
        edit_account,
        name="acct_edit",
        prefix=PEOPLE_PREFIX
    ),
]
