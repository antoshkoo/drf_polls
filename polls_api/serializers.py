from rest_framework import serializers

from polls.models import Poll, PollsQuestion, PollsAnswers


class AnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollsAnswers
        fields = ('id', 'answer_text')


class PollDetailSerializer(serializers.ModelSerializer):
    #answers = AnswerDetailSerializer(many=True, )

    class Meta:
        model = Poll
        fields = ('id', 'name', 'description', 'date_start', 'date_end')


class QuestionDetailSerializer(serializers.ModelSerializer):
    answers = AnswerDetailSerializer(many=True, )

    class Meta:
        model = PollsQuestion
        fields = ('id', 'question_type', 'question_text', 'answers', 'poll_id')


class AnswerDetail(serializers.ModelSerializer):
    class Meta:
        model = PollsAnswers
        fields = '__all__'


class QuestionDetail(serializers.ModelSerializer):
    class Meta:
        model = PollsQuestion
        fields = ('id', 'question_type', 'question_text', 'poll_id')


class PollListSerializer(serializers.ModelSerializer):
    questions = QuestionDetailSerializer(many=True)

    class Meta:
        model = Poll
        fields = ('id', 'name', 'description', 'date_start', 'date_end', 'questions')