from django.test import TestCase, Client
from django.urls import reverse
from profiles import models
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.register_url = reverse('register')
        self.edit_url = reverse('edit_user', args=[1])
        self.delete_url = reverse('delete_user', args=[1])
        self.User1 = models.User.objects.create(
            username='test',
            email='test@testemail.com',
            password='testpassword',
        )

    def test_login_user_view_GET(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/login.html')
    
    def test_register_user_view_GET(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/register_user.html')

    def test_edit_user_view_GET(self):
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'authenticate/edit_profile.html')

    def test_delete_user_view_GET(self):
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'authenticate/profile_confirm_delete.html')

    def test_register_user_POST_creates_new_user(self):
        response = self.client.post(self.register_url, {
            'role':'Tenant'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.User1.role, 'Tenant')
