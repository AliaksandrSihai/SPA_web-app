from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from habit.models import Award
from users.models import User


class TestAward(APITestCase):
    """ Testing award CRUD """

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='anonym@sky.ru',
            first_name='ww',
            last_name='SkyPro',
            is_staff=False,
            is_superuser=True,
        )
        self.access_token = str(AccessToken.for_user(self.user))
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        self.award = Award.objects.create(title='шоколад')
        self.url = 'http://127.0.0.1:8000/award/'

    def test_successful_authorization(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_award(self):
        data = {
            'title': "Отдых"
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        award = Award.objects.last()
        self.assertEqual(award.title, 'Отдых')

    def test_update_award(self):
        data = {
            'title': "Отдых"
        }
        self.assertEqual(self.award.title, 'шоколад')
        response = self.client.put(f'{self.url}{self.award.pk}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        award = Award.objects.last()
        self.assertEqual(award.title, 'Отдых')

    def test_retrieve_award(self):
        response = self.client.get(f'{self.url}{self.award.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        award = Award.objects.last()
        self.assertEqual(award.title, 'шоколад')

    def test_list_award(self):
        award_2 = Award.objects.create(title='шоколад')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        award = Award.objects.last()
        self.assertEqual(award.title, award_2.title)

    def test_delete_award(self):
        award = Award.objects.all()
        self.assertEqual(award.count(), 1)
        response = self.client.delete(f'{self.url}{self.award.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        award = Award.objects.all()
        self.assertEqual(award.count(), 0)
