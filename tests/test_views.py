from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

#run the code using python manage.py test

class LoginTestCase(TestCase):
    # The setUp method is run before each test method
    def setUp(self):
        # Create a test user and a client to make requests to the app
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='password'
        )

    def test_successful_login(self):
        # Positive test: Verifies that a user with valid login credentials can successfully log in and is authenticated.

        # Make a POST request to the login view with valid login credentials
        response = self.client.post(
            reverse('login'),
            {'username': 'testuser', 'password': 'password'}
        )
        # Assert that the response is a redirect to the home page
        self.assertRedirects(response, reverse('home'))
        # Assert that the user is authenticated
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_unsuccessful_login(self):
        # Negative test: Verifies that a user with invalid login credentials cannot log in and receives an appropriate error message.

        # Make a POST request to the login view with invalid login credentials
        response = self.client.post(
            reverse('login'),
            {'username': 'testuser', 'password': 'wrongpassword'}
        )
        # Assert that the response status code is 200 (indicating a successful request)
        self.assertEqual(response.status_code, 200)
        # Assert that the response contains the error message "Please enter a correct username and password."
        self.assertContains(response, 'Please enter a correct username and password.')
        # Assert that the user is not authenticated
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_logout(self):
        # Positive test: Verifies that a logged-in user can successfully log out and is not authenticated.

        # Log in the test user using the client.login method
        self.client.login(username='testuser', password='password')
        # Make a GET request to the logout view
        response = self.client.get(reverse('logout'))
        # Assert that the response is a redirect to the home page
        self.assertRedirects(response, reverse('home'))
        # Assert that the user is not authenticated
        self.assertFalse(response.wsgi_request.user.is_authenticated)