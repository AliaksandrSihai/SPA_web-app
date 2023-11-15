from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from django.urls import reverse
from habit.models import Habit
from users.models import User


class TestHabit(APITestCase):
    """ Testing for model's Habit"""

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
            duration="2023-11-20T11:37:58Z",
            is_pleasant=False,
            is_public=True,
            user=self.user,
            award=None,
            related_habit=None
        )

    def test_successful_authorization(self):
        response = self.client.get(reverse('habit:habit_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_habit(self):
        habits = Habit.objects.all()
        self.assertEqual(habits.count(), 1)
        data = {
            'time_to_complete': 2,
            'title': 'Cон',
            'place': 'дом',
            'action': 'Лечь спать',
            'start_time': "2023-11-14T15:58:00Z",
            'finish_time': "2023-11-14T21:31:36Z",
            'frequency': 1,
            'duration': "2023-11-20T11:37:58Z",
            'is_pleasant': False,
            'is_public': True,
            'user': self.user.pk,
            'award': '',
            'related_habit': ''
        }

        response = self.client.post(reverse('habit:habit_create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        habits = Habit.objects.all()
        self.assertEqual(habits.count(), 2)
        last_habit = Habit.objects.last()
        self.assertEqual(last_habit.title, 'Cон')

    def test_habit_put_update(self):
        data = {
            'time_to_complete': 2,
            'title': 'Гулять',
            'place': 'дом',
            'action': 'Идти гулять',
            'start_time': "2023-11-15T15:58:00Z",
            'finish_time': "2023-11-15T21:31:36Z",
            'frequency': 2,
            'duration': "2023-11-19T11:37:58Z",
            'is_pleasant': True,
            'is_public': True,
            'user': self.user.pk,
            'award': '',
            'related_habit': ''
        }
        response = self.client.put(reverse('habit:habit_update', args=[self.habit.pk]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        habit = Habit.objects.get(pk=self.habit.pk)
        self.assertEqual(habit.title, 'Гулять')

    def test_habit_list(self):
        Habit.objects.create(
            time_to_complete=2,
            title='Cон',
            place='дом',
            action='Лечь спать',
            start_time="2023-11-14T15:58:00Z",
            finish_time="2023-11-14T21:31:36Z",
            frequency=1,
            duration="2023-11-20T11:37:58Z",
            is_pleasant=False,
            is_public=True,
            user=self.user,
            award=None,
            related_habit=None
        )
        response = self.client.get(reverse('habit:habit_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        habit = Habit.objects.all()
        self.assertEqual(habit.count(), 2)

    def test_habit_destroy(self):
        habit = Habit.objects.all()
        self.assertEqual(habit.count(), 1)
        response = self.client.delete(reverse('habit:habit_destroy', args=[self.habit.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        habit = Habit.objects.all()
        self.assertEqual(habit.count(), 0)
