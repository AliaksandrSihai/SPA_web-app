from rest_framework import serializers
from rest_framework.validators import ValidationError
from habit.models import Habit, Award
from habit.validators import time_to_complete_validation


class HabitSerializer(serializers.ModelSerializer):
    """ Сериалайзер для привычки """
    time_to_complete = serializers.IntegerField(validators=[time_to_complete_validation], read_only=True)

    def validate(self, data):
        data = super().validate(data)

        frequency = data.get('frequency')
        duration = data.get('duration')
        if frequency < 1 and duration >= 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')

        award = data.get('award')
        related_habit = data.get('related_habit')
        if award and related_habit:
            raise ValidationError('Невозможен одновременный выбор связанной привычки и указания вознаграждения')

        is_pleasant = data.get('is_pleasant')
        if related_habit and is_pleasant is False:
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')

        if is_pleasant and (award or related_habit):
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')

        time_to_complete = data.get('time_to_complete')
        if time_to_complete > 2:
            raise ValidationError('Время выполнения не должно превышать 2 минуты')

        return data

    class Meta:
        model = Habit
        fields = '__all__'


class AwardSerializer(serializers.ModelSerializer):
    """ Сериалайзер для вознаграждения """
    class Meta:
        model = Award
        fields = '__all__'
