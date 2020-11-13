from django.contrib import admin
from django.urls import path, include
from polls.views import *


app_name = 'poll'
urlpatterns = [
    path('poll/create/', PollCreateView.as_view()),
    path('all/', PollListView.as_view()),
    path('poll/detail/<int:pk>', PollDetailView.as_view()),
    path('question/create/', QuestionCreateView.as_view()),
    path('question/detail/<int:pk>', QuestionDetailView.as_view()),
    path('answer/create/', AnswerCreateView.as_view()),
    path('answer/detail/<int:pk>', AnswerDetailView.as_view()),
]