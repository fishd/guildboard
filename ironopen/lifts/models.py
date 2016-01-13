# from django.db import models


# class Submission(models.Model):
#     class Meta:
#         ordering = ("-time_posted",)

#     lifter = models.ForeignKey('people.Lifter')

#     # Controls whether people outside my gym can see this
#     visible = models.BooleanField(default=True)

#     comments = models.TextField()
#     record = models.OneToOneField('records.Record')
#     image_link = models.URLField()
#     time_posted = models.DateTimeField()
#     post_title = models.CharField(max_length=200)

#     def save(self):
#         title = "{username} - {lift_type}: {weight} x {reps}"
#         related_user = self.lifter.user
#         record = self.record
#         self.post_title = title.format(
#             username=related_user.username,
#             lift_type=record.lift_type,
#             weight=record.weight,
#             reps=record.reps
#         )
#         super(Entry, self).save()

#     def get_absolute_url(self):
#         return "entries/{0}".format(self.id)
