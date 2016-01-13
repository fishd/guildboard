from collections import OrderedDict
from django.db import models

class Submission(models.Model):
    ALL_LIFTS = (
        ('Powerlifting', (
            ('Squat', 'Squat'),
            ('Bench', 'Bench'),
            ('Deadlift', 'Deadlift'))
        ),
        ('Weightlifting',  (
            ('Snatch', 'Snatch'),
            ('Clean and Jerk', 'Clean and Jerk'))
        ),
    )

    UNITS = (
        ("LB", "pounds"),
        ("KG", "kilograms")
    )

    approved = models.BooleanField(default=False)
    lift_type = models.CharField(choices=ALL_LIFTS, max_length=50)
    weight = models.IntegerField()
    unit = models.CharField(max_length=2, choices=UNITS)
    date_completed = models.DateField()
    lifter = models.ForeignKey("people.Lifter", related_name="records")
    video_link = models.URLField()

    @staticmethod
    def records():
        return Submission.objects.filter(approved=True)

    @property
    def as_row(self):
        return {
            "Type": self.lift_type,
            "Weight":"{0}{1}s".format(self.weight, self.unit.lower()),
            "Date": self.date_completed.strftime("%b %d, %Y"),
            "Lifter": str(self.lifter)
        }
