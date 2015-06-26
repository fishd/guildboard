from django.contrib import admin

from .models import Gym, Lifter, Federation

admin.site.register(Gym)
admin.site.register(Lifter)
admin.site.register(Federation)
