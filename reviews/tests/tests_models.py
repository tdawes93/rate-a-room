from django.test import TestCase
from django.contrib.auth.models import User
from reviews.models import Review, Property


class ReviewTest(TestCase):
    """
    Test class to test the Review class found in reviews.models
    """
    def setUp(self):
        user = User.objects.create(username='testuser')
        property = Property.objects.create(
            title='Test Property',
            address_postcode='AB12CD',
            type_of_property=1,
            ll_or_ea=user
        )
        self.review1 = Review.objects.create(
            title='Review 1',
            condition_of_property=2,
            quality_of_landlord=4,
            rate_the_neighbourhood=5,
            value_for_money=4,
            standard_of_amenities_nearby=1,
            user=user,
            property=property,
        )

    def test_overall_rating_is_integer_average_of_ratings(self):
        self.assertTrue(0 <= self.review1.overall_rating <= 5)
        print(self.review1.overall_rating)
        self.assertEqual(int(self.review1.overall_rating), 3)
