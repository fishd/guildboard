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
from guildboard.views import LoginRequiredView

from people.models import Gym, Federation, Lifter, JoinGymRequest
from people import forms


def edit_account(request):
    # form_class = forms.AccountForm
    # template_name= "account.html"
    # success_url = reverse_lazy("acct_edit")

    user_lifter = request.user.lifter

    if request.method == "POST":
        form = forms.AccountForm(request.POST)
        if form.is_valid():
            # user_lifter.bio = form.cleaned_data['bio']
            # user_lifter.location = form.cleaned_data['location']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            request.user.save()

    form = forms.AccountForm(
        initial={
            'email': request.user.email,
            # 'bio': user_lifter.bio,
            # 'location': user_lifter.location,
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
            'gyms': user_lifter.associated_gyms.all(),
            'owned_gyms': user_lifter.owned_gyms.all(),
            'form_title': 'Update account information'
        }
    )


class JoinGym(LoginRequiredView, FormView):
    form_class = forms.JoinGymForm
    template_name = "join_gym.html"
    success_url = reverse_lazy("acct_edit")

    def form_valid(self, form):
        gym = form.cleaned_data['gym']
        requestor = self.request.user.lifter.displayname
        request = JoinGymRequest(
            timestamp=datetime.datetime.now(),
            short_title="%s has requested to join %s." %
            (requestor, gym.name),
            gym=gym,
            initiating_user=self.request.user.lifter
        )
        request.save()
        messages.info(self.request, "Your request has been sent.")
        return super(JoinGym, self).form_valid(form)


class CreateGym(LoginRequiredView, FormView):
    form_class = forms.CreateGymForm
    template_name = "create_gym.html"
    success_url = reverse_lazy("acct_edit")

    def form_valid(self, form):
        form.process(self.request)
        return super(CreateGym, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateGym, self).get_context_data(**kwargs)
        context['form_title'] = "Create new gym"
        return context

    def get_form_kwargs(self):
        kwargs = super(CreateGym, self).get_form_kwargs()
        # todo: figure out why this won't fucking work
        kwargs['error_class'] = DivErrorList
        return kwargs


class CreateFederation(LoginRequiredView, View):
    pass
