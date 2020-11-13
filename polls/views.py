from django.shortcuts import render
from rest_framework import generics, filters
from polls.models import Poll, PollsQuestion, PollsAnswers
from polls.serializers import PollDetailSerializer, PollListSerializer, QuestionDetailSerializer, AnswerDetailSerializer, PollsAnswers


class PollCreateView(generics.CreateAPIView):
    serializer_class = PollDetailSerializer


class PollListView(generics.ListAPIView):
    serializer_class = PollListSerializer
    queryset = Poll.objects.all()


class PollDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PollDetailSerializer
    queryset = Poll.objects.all()


class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionDetailSerializer()


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailSerializer
    queryset = PollsQuestion.objects.all()


class AnswerCreateView(generics.CreateAPIView):
    serializer_class = AnswerDetailSerializer


class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerDetailSerializer
    queryset = PollsAnswers.objects.all()
