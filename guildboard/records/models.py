from collections import OrderedDict
from django.db import models

class Record(models.Model):
    ALL_LIFTS = (
        ('Powerlifting', (
            ('Squat', 'Squat'),
            ('Bench', 'Bench'),
            ('Deadlift', 'Deadlift'))),
        ('Olympic',  (
            ('Snatch', 'Snatch'),
            ('Clean and Jerk', 'Clean and Jerk'))),
        ('Misc', (
            ('Strict Press', 'Strict Press'),
            ('Push Press', 'Push Press'),
            ('Front Squat', 'Front Squat')))
    )

    UNITS = (
        ("LB", "pounds"),
        ("KG", "kilograms")
    )

    lift_type = models.CharField(choices=ALL_LIFTS, max_length=50)
    weight = models.IntegerField()
    unit = models.CharField(max_length=2, choices=UNITS)
    reps = models.IntegerField()
    date_completed = models.DateField()
    lifter = models.ForeignKey("people.Lifter", related_name="records")
    gym = models.ForeignKey("people.Gym", related_name="records")

    @property
    def as_row(self):
        return {
            "Type": self.lift_type,
            "Weight":"{0}{1}s".format(self.weight, self.unit.lower()),
            "Reps": self.reps,
            "Date": self.date_completed.strftime("%b %d, %Y"),
            "Lifter": str(self.lifter)
        }
            
class FederationRecord(Record):
    federation = models.ForeignKey("people.Federation")

    # Must be validated by federation owner
    validated = models.BooleanField(default=False)
    # restrict this somehow?
    # will need to compute on this data
    # what about lb vs kg?
    weight_class = models.IntegerField()

    # also restrict
    # hard code choices or allow user input?
    division = models.CharField(max_length=200)
