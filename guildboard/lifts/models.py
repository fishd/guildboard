from django.db import models


class Entry(models.Model):
    class Meta:
        ordering = ("-time_posted",)

    lifter = models.ForeignKey('people.Lifter')
    gym = models.ForeignKey('people.Gym')

    # Controls whether people outside my gym can see this
    visible = models.BooleanField(default=True)
    video_link = models.URLField()
    comments = models.TextField()
    record = models.OneToOneField('records.Record')
    image_link = models.URLField()
    time_posted = models.DateTimeField()
    post_title = models.CharField(max_length=200)

    def generate_title(self):
        title = "{first} {last} - {lift_type}: {weight} x {reps}"
        related_user = self.lifter.user
        record = self.record
        return title.format(
            first=related_user.first_name,
            last=related_user.last_name,
            lift_type=record.lift_type,
            weight=record.weight,
            reps=record.reps
        )    

    def get_absolute_url(self):
        return "entries/{0}".format(self.id)
