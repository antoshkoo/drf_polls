from django.contrib import admin
from django.urls import path, include
from polls import views as poll_views

urlpatterns = [
    path('', poll_views.home, name='home'),
    path('results/<poll_id>/', poll_views.results, name='results'),
    # path('poll/create/', poll_views.create, name='poll'),
    path('poll/<poll_id>/', poll_views.vote, name='poll'),
    path('vote/<vote_id>/', poll_views.vote_detail, name='vote'),
]
