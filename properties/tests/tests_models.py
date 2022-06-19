from django.test import TestCase
from properties.models import Property


class PropertyTest(TestCase):
    """
    Test class to test the Property class found in properties.models
    """
    def setUp(self):
        self.property1 = Property.objects.create(
            title='Property 1',
            slug='',
            address='5 Firgrove Hill, Farnham, Surrey, GU9 8LH',
            num_of_bedrooms=4,
            num_of_bathrooms=3,
            type_of_property=1,
            for_rent=False,
            )

    def test_title_has_max_length_of_100(self):
        """
        If property1 title is less than 101 characters test will pass
        """
        self.assertLessEqual(
            len(self.property1.title), 101
            )

    # def test_slug_auto_populates(self):
    #     """
    #     If slug auto populates property1 slug will be Property-1
    #     """
    #     print(self.property1.slug)
    #     self.assertEqual(self.property1.slug, 'property-1')
