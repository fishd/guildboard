import datetime
import operator

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView, TemplateView, View
from django.views.generic.edit import FormView
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy

from ironopen.forms import DivErrorList
from ironopen.views import LoginRequiredView

from people.models import Lifter
from people import forms


def edit_account(request):
    # form_class = forms.AccountForm
    # template_name= "account.html"
    # success_url = reverse_lazy("acct_edit")

    user_lifter = request.user.lifter

    if request.method == "POST":
        form = forms.AccountForm(request.POST)
        if form.is_valid():
            user_lifter.bio = form.cleaned_data['bio']
            user_lifter.location = form.cleaned_data['location']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            request.user.save()
            user_lifter.save()
            messages.success(request, "Account has been updated.")

    else:
        form = forms.AccountForm(
            initial={
                'email': request.user.email,
                'bio': user_lifter.bio,
                'location': user_lifter.location,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name
            }
        )
    return render(
        request,
        "account.html",
        {
            'form': form,
            "active": "acct",
            'form_title': 'Update account information',
            "request": request
        }
    )
