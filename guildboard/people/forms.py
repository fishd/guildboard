from guildboard.forms import (
    text_field,
    char_field,
    url_field,
    email_field,
    choice_field,
    int_field,
    boolean_field,
    model_choice_field
)
from django import forms
from people.models import Gym, Lifter
from country_codes import COUNTRIES
from guildboard.forms import DivErrorList


class AccountForm(forms.Form):
    email = email_field()
    bio = char_field
    location = char_field()
    first_name = char_field()
    last_name = char_field()    


class JoinGymForm(forms.Form):
    gym = choice_field(placeholder="Search for a gym")

    def __init__(self, *args, **kwargs):
        super(JoinGymForm, self).__init__(*args, **kwargs)
        self.fields['gym'].choices= [
            (gym.pk, gym.name) for gym in Gym.objects.all()
        ]

class CreateGymForm(forms.Form):
    name = char_field()
    # owners = model_choice_field(queryset=Lifter.objects.all())
    website = url_field(required=False)
    description = text_field(
        required=False,
        placeholder="Tell us about your gym!"
    )

    street_address = char_field(
        required=False,
        placeholder="e.g. 1234 Swole Street"
    )
    city = char_field()
    state = char_field(
        label="State, Province, or Region",
        placeholder="e.g. Kansas"
    )
    country = choice_field(
        choices=COUNTRIES,
        initial="US"
    )

    def process(self, request):
        gym = Gym(**self.cleaned_data)
        gym.save()
        initial_people = [Lifter.objects.get(user__username=request.user)]
        gym.owners = initial_people
        gym.lifters = initial_people[::]
        gym.save()
        
