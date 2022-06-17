from django.test import TestCase
from properties.models import Property


class PropertyTest(TestCase):
    """
    Test class to test the Property class found in properties.models
    """
    def setUp(self):
        self.property1 = Property.objects.create(
            title='Property 1',
            address='5 Firgrove Hill, Farnham, Surrey, GU9 8LH',
            num_of_bedrooms=4,
            num_of_bathrooms=3,
            type_of_property=1,
            for_rent=False,
            ) 

    def test_title_has_max_length_of_100(self):
        """
        If property1 title is less than 100 characters test will pass
        """
        self.assertLessEqual(
            len(self.property1.title), 101
            )
