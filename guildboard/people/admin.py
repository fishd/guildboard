from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Gym, Lifter,Notification

admin.site.register(Gym)
admin.site.register(Lifter)
# admin.site.register(Federation)
admin.site.register(Notification)


class LifterInline(admin.StackedInline):
    model = Lifter
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (LifterInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
