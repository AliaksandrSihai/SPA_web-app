## SPA web_app
- **All dependence in requirements.txt, % of coverade = 85, flake8 = 100%**

## Used stack:
- **Python 3.11**
- **Django REST framework**
- **PostgreSQL**
- **Celery**
## Test:
- **Unittest**
## Documentation:
- **Drf-yasg**
## Safety:
- **CORS**
- **JSON Web Token**

## About project
A one-page apps that informs users about their habits, a reminder is implemented using a telegram bot.
<br>Hows it works:
<br>The first step is to create a telegram bot and save its TELEGRAM_BOT_TOKEN in the .env file, the list of all other private settings is in .env_sample.
when creating a new user, email and telegram are filled in, after creating a user, you need to start a dialogue with the telegram bot (which was created in the previous step).Then the user creates his own habits, all habits can be pleasant, useful or connected by some other habit.A pleasant habit cannot have rewards, also all habits have some restrictions on the verification fields. After creating a habit, you need to install celery worker, celerybeat and add the necessary settings. Celery-beat has a periodic task that compares the value of the current time and the duration of the habit (as long as the duration is longer than the current time, it will be executed), after which the start time of the habit is checked, if the current time falls between the start and the finish, then the existence of a log about sending this habit is checked (to clarify the number sent notifications), and if the time of the last sending is greater than or equal to the period between notifications, then a message is sent to the user that it is time to perform some action.

## 
Первым шагом вам нужно создать telegram-бота и сохранить его TELEGRAM_BOT_TOKEN в файле .env, список всех остальных приватных настроек находится в .env_sample.
при создании нового пользователя заполняется электронная почта и telegram, после создания пользователя нужно начать диалог с  telegram-бот(который был создан на предыдущем шаге).Потом пользователь создаёт свои привычки, все привычки могут быть приятными, полезными или связанными какой-либо другой привычкой.Приятная привычка не может иметь награды, также все привычки имеют некоторые ограничения по полям проверки. После создания привычки необходимо установить celery worker, celerybeat и добавить необходимые настройки. В celery-beat есть периодическая задача, которая сравнивает значение текущего времени и продолжительности привычки(пока продолжительность будет больше чем текущее время,она будет выполняться),после проверяется время начала выполнения привычки, если текущее время попадает в промежуток между началом и концом ,то проверяется существование лога об отправке данной привычки(для уточнения количества отправленных уведомлений), и если время последней отправки будет больше или равно периоду между уведомлениями,то отправляется сообщение пользователю и том,что пора выполнить какое-то действие.

## Models:
- **Habit**
- **Award**
- **Log**
- **User**



