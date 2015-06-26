import operator

from django.shortcuts import render
from django.http import (
    HttpResponse,
    Http404,
    HttpResponseRedirect
)
from django.views.generic import ListView, TemplateView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.db.models import Q

from guildboard.views import LoginRequiredView


class GymRecords(LoginRequiredView, TemplateView):
    template_name = 'record_base.html'

    def get_context_data(self, **kwargs):
        context = super(GymRecords, self).get_context_data(**kwargs)        
        context['rows'] = []

        lifter_gyms = self.request.user.lifter.associated_gyms.all()
        gym_records = []
        for gym in lifter_gyms:
            for record in gym.records.all():
                context['rows'].append(record.as_row)

        return context

