from django.test import TestCase, Client
from django.urls import reverse
from profiles.models import User
from properties import models
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.add_property_url = reverse('add_property')
        self.property_detail = reverse(
            'property_detail', args=['some-house-ab1-2cd'])
        self.property_like = reverse('property_like', args=['some-slug'])
        self.edit_property = reverse('edit_property', args=['some-slug'])
        self.delete_property = reverse('delete_property', args=['some-slug'])
        self.User1 = User.objects.create(
            username='test',
            email='test@testemail.com',
            password='testpassword',
        )
        self.Property = models.Property.objects.create(
            title='Some House',
            address_postcode='AB1 2CD',
            type_of_property='Flat',
            status=1,
            ll_or_ea=self.User1,
        )

    def test_add_property_GET(self):
        response = self.client.get(self.add_property_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add-property.html')

    def test_property_detail_view_GET(self):
        response = self.client.get(self.property_detail)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'property-detail.html')

    # def test_edit_user_view_GET(self):
    #     response = self.client.get(self.edit_url)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTemplateUsed(response, 'authenticate/edit_profile.html')

    # def test_delete_user_view_GET(self):
    #     response = self.client.get(self.delete_url)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTemplateUsed(response, 'authenticate/profile_confirm_delete.html')

    # def test_register_user_POST_creates_new_user(self):
    #     response = self.client.post(self.register_url, {
    #         'role':'Tenant'
    #     })
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(self.User1.role, 'Tenant')
