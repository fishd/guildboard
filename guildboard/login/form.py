from guildboard.forms import *
from django import forms


class EmailForm(forms.Form):
    EMAIL = forms.EmailField(
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'form-control',
                'name': "EMAIL",
            }
        ),
    )


class LoginForm(forms.Form):

    email = char_field(
        label="Email",
        max_length=30,
        placeholder="Username"
    )
    password = password_field(
        label="Password",
        placeholder="Password"

    )


class RegistrationForm(forms.Form):
    email = email_field(
        label="Email",
        max_length=100,
    )
    password = password_field()
    confirm_password = password_field()
    first_name = char_field(
        max_length=200,
    )
    last_name = char_field(
        max_length=200,
    )

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        if not cleaned_data.get("password") == cleaned_data.get("confirm_password"):
            raise forms.ValidationError("Passwords entered do not match.")
