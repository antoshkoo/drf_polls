from django.contrib import admin
from django.contrib.admin import ModelAdmin

from polls.models import Poll, PollsQuestion, PollsAnswers, PollsUserAnswers


# Register your models here.


@admin.register(PollsQuestion, PollsAnswers, PollsUserAnswers)
class PollAdmin(ModelAdmin):
    pass


@admin.register(Poll)
class PollAdmin(ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['date_start ']
        else:
            return []

