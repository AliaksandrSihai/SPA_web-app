from datetime import datetime, timezone
from celery import shared_task
from habit.models import Habit, Log
from habit.service import telegram_sent_notification


@shared_task
def check_time():
    """ Проверка по времени для habit """
    now = datetime.now(timezone.utc)
    habit = Habit.objects.all()
    for x in habit:
        try:
            if x.start_time <= now <= x.finish_time:
                while x.duration != 0:
                    x.duration -= 1
                    if x.duration <= 0:
                        break
                    frequency = 0
                    period_per_day = 0
                    while x.frequency >= frequency and x.period_per_day >= period_per_day:
                        status = telegram_sent_notification(x.user.telegram, x.action)
                        frequency += 1
                        period_per_day += 1
                        Log.objects.create(habit=x.title,
                                           user=x.habit_log.user.email,
                                           status_response=status)
        except ValueError:
            print("Что-то пошло не так")
            Log.objects.create(habit=x.title,
                               user=x.habit_log.user.email,
                               status_response='error')
