import datetime

from django import forms

from .models import Entry
from guildboard.forms import (
    text_field,
    url_field,
    choice_field,
    int_field,
)


class EntryForm(forms.Form):
    lift_type = choice_field(choices=Entry.ALL_LIFTS)
    weight = int_field(min_value=1, label="Weight in pounds")
    reps = int_field(min_value=1)

    video_link = url_field(required=False)
    comments = text_field(required=False)


    def edit_existing_entry(self, entry):
        for field in self.entry_fields:
            setattr(entry, getattr(self.cleaned_data, field))

        for field in self.record_fields:
            setattr(entry.record, getattr(self.cleaned_data, field))

    def record_entry(self, lifter):
        cleaned_data = self.cleaned_data

        entry = Entry(
            **self.cleaned_data
        )
        entry.date_completed = datetime.datetime.today()
        entry.lifter = lifter
        entry.unit = "LB"
        entry.lifter = lifter
        entry.record = record
        entry.save()
