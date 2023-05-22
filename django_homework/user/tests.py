from django.test import TestCase
from .models import User


class UserModelTest(TestCase):
    @classmethod
    def test_user_creation(cls):
        cls.user = User.objects.create(first_name='testuser', last_name='testlastname', age='19')

    def test_user(self):
        self.assertIsNotNone(self.user, User)


class UserViewSetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(first_name='testuser', last_name='testlastname', age='19')

    def test_get_user_detail(self):
        resp = self.client.get(f'/users/{self.user.id}/')
        self.assertEqual(resp.status_code, 200)

    def test_user_create(self):
        user_data = {
            'first_name': 'Testfitstname',
            'last_name': 'Testlastname',
            'age': '18',
        }
        rest = self.client.post('/users', data=user_data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json().get('first_name'), user_data.get('first_name'))

    def test_delete_user(self):
        resp = self.client.delete(f'/users/{self.user.id}/')
        self.assertEqual(resp.status_code, 204)
