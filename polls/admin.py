from django.contrib import admin
from django.contrib.admin import ModelAdmin

from polls.models import Poll, PollsQuestion, PollsAnswers, PollsUserAnswers


# Register your models here.


@admin.register(Poll, PollsQuestion, PollsAnswers, PollsUserAnswers)
class PollAdmin(ModelAdmin):
    pass
