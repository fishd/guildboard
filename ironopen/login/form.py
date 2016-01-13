from ironopen.forms import *

class LoginForm(forms.Form):
    
    username = char_field(
        label="Username",
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
        placeholder="Email"
    )
    username = char_field(
        label="Username",
        max_length=30,
        placeholder="Username"
    )
    password = char_field(
        label="Password",
        placeholder="Password"
    )
    first_name = char_field(
        label="First Name",
        max_length=200,
        placeholder="First Name"
    )
    last_name = char_field(
        label="Last Name",
        max_length=200,
        placeholder="Last Name"
    )
    
