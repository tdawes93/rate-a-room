from django.test import TestCase
from profiles.models import User
from properties.models import Property


class PropertyTest(TestCase):
    """
    Test class to test the Property class found in properties.models
    """
    def setUp(self):
        user = User.objects.create(username='testuser')
        self.property1 = Property.objects.create(
            title='Property 1',
            address_postcode='AB1 2CD',
            num_of_bedrooms=4,
            num_of_bathrooms=3,
            type_of_property=1,
            for_rent=False,
            ll_or_ea=user,
            )

    def test_title_has_max_length_of_100(self):
        """
        If property1 title is less than 101 characters test will pass
        """
        self.assertLessEqual(
            len(self.property1.title), 101
            )
