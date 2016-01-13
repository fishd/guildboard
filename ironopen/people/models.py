from django.db import models
from django.contrib.auth.models import User



class Lifter(models.Model):
    # lifter.records
    user = models.OneToOneField(User)
    bio = models.TextField()
    location = models.CharField(max_length=200)


    def __str__(self):
        return self.user.username

    @property
    def displayname(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

# class Notification(models.Model):
#     timestamp = models.DateTimeField()
#     short_title = models.CharField(max_length=200)
#     detailed_content = models.TextField()
#     active = models.BooleanField(default=True)
#     related_users = models.ManyToManyField(
#         'Lifter', related_name="notifications"
#     )

#     def __str__(self):
#         return self.short_title

