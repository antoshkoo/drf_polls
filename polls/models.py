from django.db import models

class Poll(models.Model):

    name = models.CharField(verbose_name='Опрос', unique=True)
