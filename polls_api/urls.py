from django.urls import path
from polls_api.views import *

urlpatterns = [
    path('all/', PollListView.as_view(), name='api_all'),
    path('poll/detail/<int:pk>', PollDetailView.as_view()),
]
