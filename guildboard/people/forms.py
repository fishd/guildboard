from guildboard.forms import (
    text_field,
    char_field,
    int_field,
    url_field,
    email_field,
    choice_field,
    model_choice_field
)
from django import forms
from country_codes import COUNTRIES
from guildboard.forms import DivErrorList


class AccountForm(forms.Form):
    email = email_field()
    bio = text_field(required=False)

    first_name = char_field()
    last_name = char_field()
    squat = int_field(required=False)
    bench = int_field(required=False)
    deadlift = int_field(required=False)
    snatch = int_field(required=False)
    clean_jerk = int_field(required=False)
    front_squat = int_field(required=False)
    push_press = int_field(required=False)
    
