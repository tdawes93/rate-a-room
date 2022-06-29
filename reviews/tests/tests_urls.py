from django.test import SimpleTestCase
from django.urls import reverse, resolve
from reviews import views


class TestUrls(SimpleTestCase):

    def test_add_review_url_is_resolved(self):
        url = reverse('add_review')
        self.assertEqual(resolve(url).func.view_class, views.ReviewCreateView)

    def test_edit_review_url_is_resolved(self):
        url = reverse('edit_review', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.ReviewUpdateView)

    def test_delete_review_url_is_resolved(self):
        url = reverse('delete_review', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.ReviewDeleteView)
