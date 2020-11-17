from rest_framework import serializers
from rest_framework import permissions

from polls.models import Poll, PollsQuestion, PollsAnswers


class AnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollsAnswers
        fields = ('id', 'answer_text')


class PollDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ('id', 'name', 'description', 'date_start', 'date_end')
        read_only_fields = ('date_start', )


class QuestionDetailSerializer(serializers.ModelSerializer):
    question_answers = AnswerDetailSerializer(many=True, )

    class Meta:
        model = PollsQuestion
        fields = ('id', 'question_type', 'question_text', 'question_answers')


class AnswerDetail(serializers.ModelSerializer):
    class Meta:
        model = PollsAnswers
        fields = '__all__'


class PollListSerializer(serializers.ModelSerializer):
    questions = QuestionDetailSerializer(many=True)

    class Meta:
        model = Poll
        fields = ('id', 'name', 'description', 'date_start', 'date_end', 'questions')