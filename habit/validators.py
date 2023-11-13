from rest_framework.validators import ValidationError


def time_to_complete_validation(value):
    """ Валидация продолжительности выполнения """
    if value > 2:
        raise ValidationError("Время выполнения не должно превышать 2 минуты")
