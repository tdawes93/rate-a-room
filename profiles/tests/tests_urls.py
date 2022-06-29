from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles import views


class TestUrls(SimpleTestCase):

    def test_login_user_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, views.LoginUserView)

    def test_logout_user_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, views.logout_user)

    def test_register_user_url_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, views.RegisterUser)

    def test_edit_user_url_is_resolved(self):
        url = reverse('edit_user', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.EditUser)

    def test_delet_user_url_is_resolved(self):
        url = reverse('delete_user', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.DeleteUser)
