from django.contrib.auth.models import User
from django.db import models
from datetime import datetime



class Poll(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название', unique=True)
    date_start = models.DateTimeField(verbose_name='Дата начала', default=datetime.today())
    date_end = models.DateTimeField(verbose_name='Дата окончания', default=None)
    description = models.TextField(verbose_name='Описание')
    user_id = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

class PollsQuestion(models.Model):
    QUESTION_TYPE = (
        ('Text', 'Текст'),
        ('Checkbox', 'Чекбокс'),
        ('Radio', 'Радио'),
    )
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_type = models.CharField(max_length=50, verbose_name='Тип вопроса', choices=QUESTION_TYPE)
    question_text = models.CharField(max_length=200, verbose_name='Текст вопроса')


class PollsAnswers(models.Model):
    pass
    user_id = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    question_id = models.ForeignKey(PollsQuestion, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=500, verbose_name='Вариант ответа')


class PollsUserAnswers(models.Model):
    user_id = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    question_id = models.ForeignKey(PollsQuestion, on_delete=models.CASCADE)
    user_answer = models.TextField(verbose_name='Ответ')

# https://www.youtube.com/watch?v=C6S3dMt1s_M&t=485s&ab_channel=loftblog
# 1:47 создание авторизации

# https://www.youtube.com/watch?v=ZSQ_GxURmD4&ab_channel=SeniorPomidorDeveloper&t=289s
# мини курс джанго