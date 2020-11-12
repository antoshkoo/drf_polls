from rest_framework import serializers
from polls.models import Poll


class PollDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'
