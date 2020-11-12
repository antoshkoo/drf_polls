from django.shortcuts import render
from rest_framework import generics
from polls.serializers import PollDetailSerializer


class PollCreateView(generics.CreateAPIView):
    serializer_class = PollDetailSerializer