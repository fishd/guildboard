from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic import  View
from django.contrib.auth.decorators import login_required


class LoginRequiredView(View):

    @classmethod
    def as_view(cls, **kwargs):
        return login_required(
            super(LoginRequiredView, cls).as_view(**kwargs),
            login_url='/login/'
        )

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['request'] = self.request
        return context

