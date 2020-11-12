from django.contrib import admin
from django.urls import path, include
from polls.views import *

app_name = 'poll'
urlpatterns = [
    path('poll/create', PollCreateView.as_view())
]