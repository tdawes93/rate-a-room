from django.test import SimpleTestCase
from django.urls import reverse, resolve
from properties import views


class TestUrls(SimpleTestCase):

    def test_add_property_url_is_resolved(self):
        url = reverse('add_property')
        self.assertEqual(resolve(url).func.view_class, views.PropertyCreateView)

    def test_property_detail_url_is_resolved(self):
        url = reverse('property_detail', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, views.PropertyDetail)

    def test_property_like_url_is_resolved(self):
        url = reverse('property_like', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, views.PropertyLike)

    def test_edit_property_url_is_resolved(self):
        url = reverse('edit_property', args=['some-slug'])
        self.assertEqual(
            resolve(url).func.view_class, views.PropertyUpdateView)

    def test_delete_property_url_is_resolved(self):
        url = reverse('delete_property', args=['some-slug'])
        self.assertEqual(
            resolve(url).func.view_class, views.PropertyDeleteView)
