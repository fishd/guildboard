"""
Bandaid solution to reduce bootstrap boilerplate until
I either incorporate django crispy-forms or make my own
damn templatetags.
"""
from django import forms
from django.forms.utils import ErrorList


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return ('<div class="form_error">%s</div>' %
                ''.join(['<p class="text-danger bg-danger">%s</p>' %
                        e for e in self]))


def text_field(**kwargs):
    return forms.CharField(
        widget=forms.widgets.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '3',
                'placeholder': kwargs.pop('placeholder', '')
            }
        ),
        **kwargs
    )


def password_field(**kwargs):
    return forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': kwargs.pop('placeholder', '')}
        ),
        **kwargs
    )


def char_field(**kwargs):
    return forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': kwargs.pop('placeholder', '')}
        ),
        **kwargs
    )


def email_field(**kwargs):
    return forms.EmailField(
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': kwargs.pop('placeholder', '')
            }
        ),
        **kwargs
    )


def url_field(**kwargs):
    return forms.URLField(
        widget=forms.widgets.URLInput(
            attrs={
                'class': 'form-control',
                'placeholder': kwargs.pop('placeholder', '')
            }
        ),
        **kwargs
    )


def model_choice_field(**kwargs):
    return forms.ModelChoiceField(
        widget=forms.widgets.Select(
            attrs={
                'class': 'form-control select2',
                'placeholder': kwargs.pop('placeholder', '')}
        ),
        **kwargs
    )


def choice_field(**kwargs):
    return forms.ChoiceField(
        widget=forms.widgets.Select(
            attrs={
                'class': 'form-control select2',
                'placeholder': kwargs.pop('placeholder', '')}
        ),
        **kwargs
    )


def decimal_field(**kwargs):
    return forms.DecimalField(
        decimal_places=2,
        widget=forms.widgets.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': kwargs.pop('placeholder', '')
            }
        ),
        **kwargs
    )

def int_field(**kwargs):
    return forms.IntegerField(
        widget=forms.widgets.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': kwargs.pop('placeholder', '')
            }
        ),
        **kwargs
    )


def date_field(**kwargs):
    return forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={
                'class': 'form-control datepicker',
                'placeholder': kwargs.pop('placeholder', '')
            }
        ),
        **kwargs
    )


def boolean_field(**kwargs):
    return forms.BooleanField(
        widget=forms.widgets.CheckboxInput(
            attrs={}
        ),
        **kwargs
    )
