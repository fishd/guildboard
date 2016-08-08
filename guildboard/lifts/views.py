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
from lifts.forms import EntryForm
from lifts.models import Entry


class MyEntryList(LoginRequiredMixin, ListView):
    context_object_name = 'entries'
    template_name = 'edit_entries.html'

    def get_context_data(self, **kwargs):
        context = super(MyEntryList, self).get_context_data(**kwargs)
        context['empty_text'] = "You have not made any entries."
        context['active'] = "my_list"
        context['edit'] = True
        return context

    def get_queryset(self):
        return self.request.user.lifter.entry_set.all()


class EntryDetail(LoginRequiredMixin, DetailView):
    template_name = 'entry_detail.html'
    model = Entry

class CreateEntry(LoginRequiredMixin, FormView):
    context_object_name = 'entry'
    template_name = 'create_entry.html'
    form_class = EntryForm
    success_url = reverse_lazy("lifts_manage")

    def form_valid(self, form):
        form.record_entry(self.request.user.lifter)
        return super(CreateEntry, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateEntry, self).get_context_data(**kwargs)
        context['active'] = "create"
        return context


# class EditEntry(LoginRequiredMixin, FormView):
#     context_object_name = 'entry'
#     template_name = 'edit_entry.html'
#     form_class = forms.EntryForm
#     success_url = reverse_lazy("lifts_manage")

#     def form_valid(self, form):
#         form.record_entry(self.request.user.lifter)
#         return super(EditEntry, self).form_valid(form)

#     def get_form_kwargs(self):
#         kwargs = super(EditEntry, self).get_form_kwargs()
#         kwargs['lifter'] = self.request.user.lifter
#         return kwargs

#     def get_context_data(self, **kwargs):
#         context = super(EditEntry, self).get_context_data(**kwargs)
#         context['active'] = "edit"
#         return context    
 
def edit_an_entry(request, entry_id):
    try:
        entry = Entry.objects.get(pk=entry_id)
    except Entry.objects.DoesNotExist:
        raise Http404("Specified entry not found.")
    else:
        if request.method == "POST":
            form = forms.EntryForm(request.POST)
            if form.is_valid():
                form.edit_existing_entry(entry)
    
            return HttpResponseRedirect(reverse_lazy("lifts_edit"))

        elif request.method == "GET":
            initial_values = {}
            for field in forms.EntryForm.entry_fields:
                initial_values[field] = getattr(entry, field, None)
            for field in forms.EntryForm.record_fields:
                initial_values[field] = getattr(entry.record, field, None)

            form = forms.EntryForm(
                initial=initial_values,
            )

            return render(
                request,
                "form.html",
                {
                    'form': form,
                    'form_title': 'Edit entry'
                }
            )
