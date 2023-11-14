from django.contrib import admin

from habit.models import Habit, Award, Log

# Register your models here.
admin.site.register(Habit)
admin.site.register(Award)
admin.site.register(Log)