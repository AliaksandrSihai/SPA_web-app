from django.db import models

from config import settings
from users.models import NULLABLE


# Create your models here.
class Habit(models.Model):
    """ Класс для определения привычки """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name='пользователь', related_name='user', **NULLABLE)
    title = models.TextField(verbose_name='название привычки')
    place = models.CharField(max_length=50, verbose_name='место')
    action = models.TextField(verbose_name='действие')
    start_time = models.DateTimeField(verbose_name='время начала выполнения')
    finish_time = models.DateTimeField(verbose_name='время конца выполнения')
    time_to_complete = models.IntegerField(verbose_name='время на выполнение в минутах')
    frequency = models.IntegerField(default=1, verbose_name='частота выполнения раз в день ')
    duration = models.DateTimeField(verbose_name='продолжительность')
    award = models.ForeignKey(to='Award', on_delete=models.SET_NULL, verbose_name='вознаграждение',
                              related_name='award', **NULLABLE)
    related_habit = models.ForeignKey(to='self', on_delete=models.SET_NULL,
                                      verbose_name='связанные привычки', **NULLABLE, )
    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'


class Award(models.Model):
    """ Класс для создания вознаграждений """
    title = models.TextField(verbose_name='название вознаграждения')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'вознаграждение'
        verbose_name_plural = 'вознаграждения'


class Log(models.Model):
    """ Уведомление """
    habit = models.ForeignKey(to=Habit, on_delete=models.CASCADE, verbose_name='habit', related_name='habit_log')
    user = models.EmailField(verbose_name='user')
    status_response = models.CharField(max_length=55, **NULLABLE)
    date = models.DateTimeField(auto_now_add=True, verbose_name='date')

    def __str__(self):
        return self.status_response

    class Meta:
        verbose_name = 'log'
        verbose_name_plural = 'logs'
