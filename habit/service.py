from datetime import datetime, timezone
import requests

from config import settings
from habit.models import Habit


def telegram_sent_notification(user_name, habit):
    """ Интеграция с телеграм """
    url = f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/getUpdates'
    response = requests.get(url=url)
    user_id = response.json()['result']
    for x in user_id:
        if user_name == x['message']['from']['username']:
            url_post = f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage'
            data = {
                'chat_id': x['message']['from']['id'],  # data.telegram
                'text': f'Настал час {habit}'
            }
            response = requests.post(url=url_post,
                                     data=data)
            return response.status_code
        else:
            raise ValueError('Произошла ошибка')

# def test():
#    # now = datetime.datetime.now()
#     now = datetime.now(timezone.utc)
#     habit = Habit.objects.all()
#     for x in habit:
#         if x.start_time:
#             telegramm_sent_notification(x.user.telegram, x.action)





