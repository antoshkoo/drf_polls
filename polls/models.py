from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название', unique=True)
    date_start = models.DateTimeField(verbose_name='Дата начала', auto_now_add=True)
    date_end = models.DateTimeField(verbose_name='Дата окончания', default=None)
    description = models.TextField(verbose_name='Описание')

class PollsQuestion(models.Model):
    QUESTION_TYPE = (
        'Text',
        'Checkbox'
        'Radio'
    )
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_type = models.CharField(max_length=50, verbose_name='Тип вопроса', choices=QUESTION_TYPE)
    question_text = models.CharField(max_length=200, verbose_name='Текст вопроса')

class PollsAnswers(models.Model):
    pass
    # user_id =
    question_id = models.ForeignKey(PollsQuestion, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=500, verbose_name='Вариант ответа')

class PollsUserAnswers(models.Model):
    # user_id =
    question_id = models.ForeignKey(PollsQuestion, on_delete=models.CASCADE)
    user_answer = models.TextField(verbose_name='Ответ')