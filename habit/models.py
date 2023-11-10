from django.db import models

from config import settings
from users.models import NULLABLE


# Create your models here.
class Habit(models.Model):
    """ Класс для определения привычки """

    # FREQUENCY = [
    #     ('everyday', 'everyday'),
    #     ('every_per_week', 'once_per_week'),
    #     ('once_per_week', 'once_per_week'),
    # ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name='пользователь', **NULLABLE)
    title = models.TextField(verbose_name='название привычки')
    place = models.CharField(max_length=50, verbose_name='место')
    action = models.TextField(verbose_name='действие')

    start_time = models.DateTimeField(verbose_name='время в которое необходимо выполнить')
    time_to_complete = models.IntegerField(verbose_name='время на выполнение в минутах')
    # frequency = models.CharField(max_length=255, choices=FREQUENCY, default='everyday',
    #                              verbose_name='частота выполнения')
    frequency = models.IntegerField(default=1, verbose_name='частота выполнения раз в день')
    duration = models.IntegerField(default=21, verbose_name='продолжительность в днях')

    award = models.ForeignKey(to='Award', on_delete=models.SET_NULL, verbose_name='вознаграждение',
                              related_name='award',  **NULLABLE)
    related_habit = models.ForeignKey(to='self', on_delete=models.SET_NULL,
                                      verbose_name='связанные привычки', **NULLABLE, )

    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        # unique_together = ('award', 'related_habit')


class Award(models.Model):
    """ Класс для создания вознаграждений """
    title = models.TextField(verbose_name='название вознаграждения')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'вознаграждение'
        verbose_name_plural = 'вознаграждения'
