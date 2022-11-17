from django.contrib.messages import api
from django.test import TestCase
import json
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, URLPatternsTestCase

from .models import CustomUser


# Create your tests here.
class UserTest(APITestCase, URLPatternsTestCase):
    """ Test module for User """

    urlpatterns = [
        path('api/auth/', include('system_user.urls')),
    ]

    def setUp(self):
        self.user1 = CustomUser.objects.create_user(
            username='shalitha',
            password='test',
        )

        self.admin = CustomUser.objects.create_superuser(
            username='lakshan',
            password='admin',
        )

    def test_login(self):
        """ Test if a user can login and get a JWT response token """
        url = reverse('login')
        data = {
            'username': 'Lalith',
            'password': 'sliit2021'
        }
        response = self.client.post(url, data)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data['success'], True)
        self.assertTrue('access' in response_data)

    def test_user_registration(self):
        """ Test if a user can register """
        url = reverse('register')
        data = {
            'username': 'shalitha',
            'password': 'test',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_all_users_as_admin(self):
        """ Test fetching all users. Restricted to admins """
        # Setup the token
        url = reverse('login')
        data = {'username': 'shalitha', 'password': 'admin'}
        response = self.client.post(url, data)
        login_response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in login_response_data)
        token = login_response_data['access']

        # Test the endpoint
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = client.get(reverse('users'))
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CustomUser.objects.count(), len(response_data['users']))

    def test_access_denied_all_users(self):
        """ Test fetching all users. Restricted to admins """
        # Setup the token
        url = reverse('login')
        data = {'username': 'shalitha', 'password': 'test'}
        response = self.client.post(url, data)
        login_response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in login_response_data)
        token = login_response_data['access']

        # Test the endpoint
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = client.get(reverse('users'))
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(response_data['success'])
