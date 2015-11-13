from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    timestamp = models.DateTimeField()
    short_title = models.CharField(max_length=200)
    detailed_content = models.TextField()
    active = models.BooleanField(default=True)
    related_users = models.ManyToManyField(
        'Lifter', related_name="notifications"
    )

    def __str__(self):
        return self.short_title


class JoinGymRequest(Notification):
    initiating_user = models.ForeignKey('Lifter')
    gym = models.ForeignKey('Gym')


class Lifter(models.Model):

    user = models.OneToOneField(User)
    # bio
    # location

    # lifter.entry_set
    # lifter.competitive_federations
    # lifter.owned_federations
    # lifter.owned_gyms
    # lifter.associated_gyms

    is_owner = models.BooleanField(default=False)

    @property
    def all_gyms(self):
        return list(self.owned_gyms.all()) + list(self.associated_gyms.all())

    def __str__(self):
        return self.user.username

    # @property
    # def PRs(self):
    #     max_squat = self.records.filter(lift_type="Squat").order_by("weight")[-1]
    #     PRs = {}

    @property
    def displayname(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)


class Federation(models.Model):
    name = models.CharField(max_length=200)
    acronym = models.CharField(max_length=30)
    lifters = models.ManyToManyField(
        'Lifter', related_name='competitive_federations'
    )

    # When this field is set, we should
    # also set is_owner = True on the lifter
    owners = models.ManyToManyField('Lifter', related_name='owned_federations')
    website = models.URLField()


class Gym(models.Model):
    name = models.CharField(max_length=200)
    # When this field is set, we should
    # also set is_owner = True on the lifter
    owners = models.ManyToManyField('Lifter', related_name='owned_gyms')
    lifters = models.ManyToManyField('Lifter', related_name='associated_gyms')
    website = models.URLField()
    description = models.TextField()

    # Perform validation on all of these
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name
