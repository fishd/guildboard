from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Lifter

admin.site.register(Lifter)


class LifterInline(admin.StackedInline):
    model = Lifter
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (LifterInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
