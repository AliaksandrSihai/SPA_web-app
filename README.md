## SPA web_app
- **All dependence in requirements.txt, % of coverade = 85, flake8 = 100%**

## Used stack:
- **Language:  Python 3.11**
- **Django rest framework**
- **Database: PostgreSQL**
- **Celery**
## Test:
- **Unittest**
## Models:
- **Habit**
- **Award**
- **Log**
- **User**

## About project
A one-page apps that informs users about their habits, a reminder is implemented using a telegram bot.
<br>Hows it works:
The first step is to create a telegram bot and save its TELEGRAM_BOT_TOKEN in the .env file, the list of all other private settings is in .env_sample.
<br>When creating a new user, the email and telegram must be filled in, the telegram bot automatically sends him a welcome message. After creating a new user, he creates his own habits, all habits can be pleasant, useful or related to some other habit.A pleasant habit cannot have rewards, also all habits have some restrictions on the verification fields. After creating a habit, you need to install celery worker and celerybeat. Celery-beat has one task that checks the time to remind you of a habit, if the time has come, celery-beat gives this task to the employee who started the communication function with the telegram bot, and the bot sends a notification to the user about the time of any habit.

## 
Первым шагом вам нужно создать telegram-бота и сохранить его TELEGRAM_BOT_TOKEN в файле .env, список всех остальных приватных настроек находится в .env_sample.
при создании нового пользователя обязательно заполняется электронная почта и telegram, telegram-бот автоматически отправляет ему приветственное сообщение. После создания нового пользователя он создает свои привычки, все привычки могут быть приятными, полезными или связанными какой-либо другой привычкой.Приятная привычка не может иметь награды, также все привычки имеют некоторые ограничения по полям проверки. После создания привычки вам необходимо установить celery worker и celerybeat. В celery-beat есть одна задача, которая проверяет время, чтобы напомнить о привычке, если пришло время, celery-beat дает эту задачу работнику, который запустил функцию связи с telegram-ботом, и бот отправляет уведомление пользователю о времени выполнения какой-либо привычки.





