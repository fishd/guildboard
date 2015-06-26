import datetime

from django import forms

from lifts.models import Entry
from records.models import Record
from guildboard.forms import (
    text_field,
    model_choice_field,
    char_field,
    url_field,
    email_field,
    choice_field,
    int_field,
    boolean_field,
)

    
class EntryForm(forms.Form):
    entry_fields = ['gym', 'visible', 'video_link', 'image_link', 'comments']
    record_fields = ['lift_type', 'weight','unit', 'reps', 'gym']

    gym = model_choice_field(queryset=None)
    visible = boolean_field(
        label=("Make this entry visible to people outside of"
               " my gym"),
        required=False,
        initial=True
    )
    lift_type = choice_field(choices=Record.ALL_LIFTS)
    weight = int_field(min_value=1)
    unit = choice_field(choices=Record.UNITS)
    reps = int_field(min_value=1)

    video_link = url_field(required=False)
    image_link = url_field(required=False)
    comments = text_field(required=False)
    

    def __init__(self, **kwargs):
        lifter = kwargs.pop("lifter")

        super(EntryForm, self).__init__(**kwargs)
        self.fields['gym'].queryset = lifter.associated_gyms
        
    def edit_existing_entry(self, instance):
        pass
    def record_entry(self, lifter):
        cleaned_data = self.cleaned_data

        entry = Entry(
            **{field: cleaned_data.get(field) for field in self.entry_fields}
        )
        record = Record(
            **{field: cleaned_data.get(field) for field in self.record_fields}
        )
        record.date_completed = datetime.datetime.today()
        record.lifter = lifter
        record.save()

        entry.time_posted = datetime.datetime.now()
        entry.lifter = lifter
        entry.record = record
        entry.post_title = entry.generate_title()
        entry.save()


            
