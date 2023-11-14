from rest_framework import serializers
from rest_framework.validators import ValidationError
from habit.models import Habit, Award, Log
from habit.validators import time_to_complete_validation
from datetime import datetime, timezone, timedelta


class HabitSerializer(serializers.ModelSerializer):
    """ Сериалайзер для привычки """
    time_to_complete = serializers.IntegerField(validators=[time_to_complete_validation])

    def validate(self, data):
        data = super().validate(data)

        frequency = data.get('frequency')
        duration = data.get('duration')
        now = datetime.now(timezone.utc)
        if frequency <= 1 and duration > now + timedelta(days=6):
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')

        award = data.get('award')
        related_habit = data.get('related_habit')
        if award and related_habit:
            raise ValidationError('Невозможен одновременный выбор связанной привычки и указания вознаграждения')

        is_pleasant = data.get('is_pleasant')
        if related_habit is not None and not related_habit.is_pleasant:
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')

        if is_pleasant and (award or related_habit):
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')

        start_time = data.get('start_time')
        finish_time = data.get('finish_time')
        if start_time > finish_time:
            raise ValidationError('Время начала не может быть больше времени окончания')

        return data

    class Meta:
        model = Habit
        fields = '__all__'


class AwardSerializer(serializers.ModelSerializer):
    """ Сериалайзер для вознаграждения """
    class Meta:
        model = Award
        fields = '__all__'


class LogSerializer(serializers.ModelSerializer):
    """ Сериалайзер логов """

    class Meta:
        model = Log
        fields = '__all__'
