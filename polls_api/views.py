from rest_framework import generics

from polls.models import Poll
from polls_api.serializers import PollDetailSerializer, PollListSerializer


class PollCreateView(generics.CreateAPIView):
    serializer_class = PollDetailSerializer


class PollListView(generics.ListAPIView):
    serializer_class = PollListSerializer
    queryset = Poll.objects.all()


class PollDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PollDetailSerializer
    queryset = Poll.objects.all()
