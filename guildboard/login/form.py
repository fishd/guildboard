from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Username'}),
    )

class RegistrationForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    username = forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )
    first_name = forms.CharField(
        label="First Name",
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    
