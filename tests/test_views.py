from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse


class LoginTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='usertest',
            password='passtest'
        )

    # check if login page loads correctly using the right template.
    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

.
    # assure that the user can login using valid credentials forwarding to the home page.
    def test_login_success(self):
        response = self.client.post(reverse('login'), {
            'username': 'usertest',
            'password': 'passtest'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    # assure that the user cannot log in using invalid credentials, and shows a message error at login page
    def test_login_failure(self):
        response = self.client.post(reverse('login'), {
            'username': 'wronguser',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertContains(response, 'Please enter a correct username and password.')
