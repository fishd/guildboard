from django.db import models
from django.contrib.auth.models import User

class Lifter(models.Model):

    user = models.OneToOneField(User)
    bio = models.TextField(null=True, blank=True)
    squat = models.IntegerField(null=True)
    front_squat = models.IntegerField(null=True)
    bench = models.IntegerField(null=True)
    deadlift = models.IntegerField(null=True)
    snatch = models.IntegerField(null=True)
    clean_jerk = models.IntegerField(null=True)
    front_squat = models.IntegerField(null=True)
    push_press = models.IntegerField(null=True)


    def __str__(self):
        return self.user.username


    @property
    def displayname(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)
