import datetime
import operator

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView, TemplateView, View
from django.views.generic.edit import FormView
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy

from guildboard.forms import DivErrorList
from django.contrib.auth.mixins import LoginRequiredMixin

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
            user_lifter.squat = form.cleaned_data['squat']
            user_lifter.bench = form.cleaned_data['bench']
            user_lifter.deadlift = form.cleaned_data['deadlift']
            user_lifter.snatch = form.cleaned_data['snatch']
            user_lifter.clean_jerk = form.cleaned_data['clean_jerk']
            user_lifter.push_press = form.cleaned_data['push_press']
            user_lifter.front_squat = form.cleaned_data['front_squat']
            user_lifter.save()
            # user_lifter.location = form.cleaned_data['location']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            request.user.save()

    else:
        form = forms.AccountForm(
            initial={
                'email': request.user.email,
                'bio': user_lifter.bio,
                # 'location': user_lifter.location,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'squat': user_lifter.squat,
                'bench': user_lifter.bench,                
                'deadlift': user_lifter.deadlift,
                'snatch': user_lifter.snatch,
                'clean_jerk': user_lifter.clean_jerk,
                'push_press': user_lifter.push_press,
                'front_squat': user_lifter.front_squat,
            }
        )
    return render(
        request,
        "account.html",
        {
            'form': form,
            "active": "acct",
            # 'gyms': user_lifter.associated_gyms.all(),
            # 'owned_gyms': user_lifter.owned_gyms.all(),
            'form_title': 'Update account information'
        }
    )
