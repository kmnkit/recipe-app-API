from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
TOKEN_URL = reverse('users:token')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicTokenApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_token_for_user(self):
        """Test that a token is created for the user"""
        payload = {'email': 'test@nomad.com',
                   'password': 'testpass', 'name': 'Test'}
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test that Token is not created if invalid credentials are given"""
        create_user(email='test@nomad.com', password='testpass', name='Test')
        payload = {'email': 'test@nomad.com', 'password': 'wrong'}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test that token is not created if user doesn't exist"""
        payload = {'email': 'test@nomad.com', 'password': 'testpass'}
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """Test that email and password are required"""
        res = self.client.post(TOKEN_URL, {'email': 'one', 'password': ''})
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
