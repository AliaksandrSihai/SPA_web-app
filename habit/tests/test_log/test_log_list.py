from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from django.urls import reverse
from habit.models import Log, Habit
from users.models import User


class TestListLog(APITestCase):
    """ Test for getting list of logs """

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='anonym@sky.ru',
            first_name='ww',
            last_name='SkyPro',
            is_staff=False,
            is_superuser=False,
        )
        self.access_token = str(AccessToken.for_user(self.user))
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        self.habit = Habit.objects.create(
            time_to_complete=2,
            title='Спорт',
            place='дом',
            action='Сделать упражнения',
            start_time="2023-11-14T14:58:00Z",
            finish_time="2023-11-14T20:31:36Z",
            frequency=1,
            duration="2023-11-28T11:37:58Z",
            is_pleasant=False,
            is_public=True,
            user=self.user,
            award=None,
            related_habit=None

        )
        self.habit_2 = Habit.objects.create(
            time_to_complete=2,
            title='Сон',
            place='дом',
            action='Лечь спать',
            start_time="2023-11-14T14:58:00Z",
            finish_time="2023-11-14T20:31:36Z",
            frequency=1,
            duration="2023-11-28T11:37:58Z",
            is_pleasant=False,
            is_public=True,
            user=self.user,
            award=None,
            related_habit=None

        )

        self.log_1 = Log.objects.create(
            habit=self.habit,
            user=self.user
        )
        self.log_2 = Log.objects.create(
            habit=self.habit_2,
            user=self.user

        )

    def test_successful_authorization(self):
        response = self.client.get(reverse('habit:habit_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_log(self):
        response = self.client.get(reverse('habit:habit_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Log.objects.count(), 2)
        log = Log.objects.last()
        self.assertEqual(log.habit.title, 'Сон')
        self.assertEqual(log.user, self.user.email)
