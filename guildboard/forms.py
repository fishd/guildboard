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
        return ('<div class="danger">%s</div>' %
                ''.join(['<div class="danger">%s</div>' % e for e in self]))

def text_field(**kwargs):
    return forms.CharField(
        widget=forms.widgets.Textarea(
            attrs={'class': 'form-control',
                    'placeholder': kwargs.pop('placeholder', '')
            }
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
        widget=forms.widgets.Textarea(
            attrs={'class': 'form-control'}
        ),
        **kwargs
    )

def url_field(**kwargs):
    return forms.URLField(
        widget=forms.widgets.URLInput(
            attrs={'class': 'form-control'}
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

def int_field(**kwargs):
    return forms.IntegerField(
        widget=forms.widgets.NumberInput(
            attrs={'class': 'form-control'}
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

def model_choice_field(**kwargs):
    return forms.ModelChoiceField(
        widget=forms.widgets.Select(
            attrs={
                'class': 'form-control select2',
                'placeholder': kwargs.pop('placeholder', '')}
        ),
        **kwargs
    )
