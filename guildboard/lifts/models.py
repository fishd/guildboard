from django.db import models


class Entry(models.Model):
    class Meta:
        ordering = ("-date_completed",)

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

    lifter = models.ForeignKey('people.Lifter')

    video_link = models.URLField()

    lifter = models.ForeignKey('people.Lifter', related_name="entries")
    lift_type = models.CharField(choices=ALL_LIFTS, max_length=50)
    weight = models.IntegerField()
    date_completed = models.DateField()



    def get_absolute_url(self):
        return "entries/{0}".format(self.id)

    def formatted_date(self):
        return self.date_completed.strftime("%b %d, %Y")
