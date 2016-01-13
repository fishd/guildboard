import operator

from django.views.generic import ListView
from django.views.generic import View
from django.db.models import Q

from guildboard.views import LoginRequiredView
from people.models import Gym, Federation, Lifter
from lifts.models import Entry


class GymEntryList(LoginRequiredView, ListView):
    context_object_name = 'entries'
    template_name = 'feed.html'

    def get_context_data(self, **kwargs):
        context = super(GymEntryList, self).get_context_data(**kwargs)
        context['active'] = 'gym'
        context['empty_text'] = (
            "No entries found for your gyms."
            " Join a gym by visiting your account settings page."
        )
        return context

    def get_queryset(self):
        q = None
        for gym in self.request.user.lifter.associated_gyms.all():
            if not q:
                q = Q(gym=gym)
            else:
                q = q | Q(gym=gym)

        if q:
            return Entry.objects.filter(q)
        else:
            return []


class PublicEntryList(ListView):
    context_object_name = 'entries'
    template_name = 'feed.html'

    def get_context_data(self, **kwargs):
        context = super(PublicEntryList, self).get_context_data(**kwargs)
        context['active'] = 'public'
        context['empty_text'] = "No public entries found."
        return context

    def get_queryset(self):
        return Entry.objects.filter(
            visible=True
        )

class FederationEntryList(LoginRequiredView, ListView):
    context_object_name = 'entries'
    template_name = 'feed.html'

    def get_context_data(self, **kwargs):
        context = super(FederationEntryList, self).get_context_data(**kwargs)
        context['active'] = 'federation'
        context['empty_text'] = (
            "No entries found for your federations."
            " Follow a federation by visiting your account settings page,"
            " or browse all public entries."
        )

        return context

    def get_queryset(self):
        user = Lifter.objects.get(user__username=self.request.user)
        user_feds = Federation.objects.filter(
            Q(lifters=user) |
            Q(owners=user)
        )
        if user_feds:
            entry_query = reduce(
                operator.or_,
                [Q(record__federation=fed) for fed in user_feds]
            )
            return Entry.objects.filter(entry_query)
        else:
            return []
