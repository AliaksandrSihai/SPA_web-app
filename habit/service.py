from datetime import datetime, timezone
import requests
from config import settings
from habit.models import Habit, Log


def telegram_sent_notification(user_name, habit):
    """ Интеграция с телеграм """
    url = f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/getUpdates'
    response = requests.get(url=url)
    user_id = response.json()['result']
    for x in user_id:
        if user_name == x['message']['from']['username']:
            url_post = f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage'
            data = {
                'chat_id': x['message']['from']['id'],
                'text': f'Настал час {habit}'
            }
            response = requests.post(url=url_post,
                                     data=data)
            return response.status_code
        else:
            raise ValueError('Произошла ошибка')


def check_habit_time():
    """ Проверка по времени для habit """
    now = datetime.now(timezone.utc)
    habits = Habit.objects.all()
    for habit in habits:
        if habit.duration > now:
            if habit.start_time <= now <= habit.finish_time:
                # try:
                if habit.habit_log.all().exists():
                    status = telegram_sent_notification(habit.user.telegram, habit.action)
                    print(habit.user.telegram)
                    print(status)
                    print(
                        f"Habit ID: {habit.title}, Start Time: {habit.start_time}, Finish Time: {habit.finish_time}, Duration: {habit.duration}")
                    print('--------------------------')
                    # for log in habit.habit_log.all():
                    #     period = ((habit.finish_time - habit.start_time) // habit.frequency).total_seconds()
                    #     if (now - log.date).total_seconds() > period:
                    #         status = telegram_sent_notification(habit.user.telegram, habit.action)
                    #         Log.objects.create(habit=habit.id, user=habit.user.email, status_response=status)
                else:
                    status = telegram_sent_notification(habit.user.telegram, habit.action)
                    Log.objects.create(habit=habit, user=habit.user.email, status_response=status)
                # except ValueError:
                #     print("Что-то пошло не так")
                #     Log.objects.create(habit=habit, user=habit.user.email, status_response='error')
