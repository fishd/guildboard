from ironopen.forms import (
    text_field,
    char_field,
    url_field,
    email_field,
    choice_field,
    model_choice_field
)
from django import forms
from people.models import Lifter
from country_codes import COUNTRIES
from ironopen.forms import DivErrorList


class AccountForm(forms.Form):
    email = email_field()
    bio = char_field()
    location = char_field()
    first_name = char_field()
    last_name = char_field()
