from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ratemyroom import views


class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('homepage')
        self.assertEqual(resolve(url).func.view_class, views.PropertyList)

    def test_search_properties_url_is_resolved(self):
        url = reverse('search_properties')
        self.assertEqual(resolve(url).func.view_class, views.SearchProperty)

    def test_search_properties_for_review_url_is_resolved(self):
        url = reverse('search_properties_for_review')
        self.assertEqual(
            resolve(url).func.view_class, views.SearchPropertyForReview)

    def test_search_form_url_is_resolved(self):
        url = reverse('search_form')
        self.assertEqual(resolve(url).func.view_class, views.SearchForm)
