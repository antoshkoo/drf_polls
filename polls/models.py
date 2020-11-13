from django.contrib.auth.models import User
from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название', unique=True)
    date_start = models.DateTimeField(verbose_name='Дата начала', auto_now=True)
    date_end = models.DateTimeField(verbose_name='Дата окончания')
    description = models.TextField(verbose_name='Описание')
    user_id = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    # @property
    # def is_expired(self):
    #     if datetime.now() > self.date_end:
    #         return True
    #     return False


class PollsQuestion(models.Model):
    QUESTION_TYPE = (
        ('text', 'Текст'),
        ('checkbox', 'Чекбокс'),
        ('radio', 'Радио'),
    )
    poll_id = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    question_type = models.CharField(max_length=50, verbose_name='Тип вопроса', choices=QUESTION_TYPE)
    question_text = models.CharField(max_length=200, verbose_name='Текст вопроса')


class PollsAnswers(models.Model):
    user_id = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    question_id = models.ForeignKey(PollsQuestion, related_name='answers',  on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=500, verbose_name='Вариант ответа')


class PollsUserAnswers(models.Model):
    user_id = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    question_id = models.ForeignKey(PollsQuestion, on_delete=models.CASCADE)
    user_answer = models.TextField(verbose_name='Ответ')