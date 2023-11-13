from rest_framework import serializers
from rest_framework.validators import ValidationError
from habit.models import Habit, Award
from habit.validators import time_to_complete_validation


class HabitSerializer(serializers.ModelSerializer):
    """ Сериалайзер для привычки """
    time_to_complete = serializers.IntegerField(validators=[time_to_complete_validation])

    def validate(self, data):
        data = super().validate(data)

        frequency = data.get('frequency')
        duration = data.get('duration')
        if frequency < 1 and duration < 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')
        period_day = data.get('period_day')
        if period_day > 12 and frequency > 1:
            raise ValidationError('Период не может быть больше 12 часов в течении одного дня')
        award = data.get('award')
        related_habit = data.get('related_habit')
        if award and related_habit:
            raise ValidationError('Невозможен одновременный выбор связанной привычки и указания вознаграждения')

        is_pleasant = data.get('is_pleasant')
        if related_habit is not None and not related_habit.is_pleasant :
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')

        if is_pleasant and (award or related_habit):
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')


        return data

    class Meta:
        model = Habit
        # fields = ('user', 'title', 'place', 'action', 'start_time', 'time_to_complete', 'frequency',
        #           'duration', 'award', 'related_habit', 'is_pleasant', 'is_public')
        fields = '__all__'


class AwardSerializer(serializers.ModelSerializer):
    """ Сериалайзер для вознаграждения """
    class Meta:
        model = Award
        fields = '__all__'
