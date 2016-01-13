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

from ironopen.views import LoginRequiredView
from .models import Submission

class Leaderboard(TemplateView):
    template_name = 'record_base.html'

    def get_context_data(self, **kwargs):
        context = super(Leaderboard, self).get_context_data(**kwargs)        
        context['rows'] = []

        for record in Submission.records():
            context['rows'].append(record.as_row)

        return context

