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

from django.contrib.auth.mixins import LoginRequiredMixin
from people.models import Lifter

class GymRecords(LoginRequiredMixin, TemplateView):
    template_name = 'record_base.html'

    def get_context_data(self, **kwargs):
        context = super(GymRecords, self).get_context_data(**kwargs)        
        lifters = Lifter.objects.all()

        context["lifters"] = lifters

        return context

