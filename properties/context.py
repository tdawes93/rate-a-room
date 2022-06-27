# Code written by Ger at Code Institue Tutor support

from django.db.models import Avg
from .models import Property


def get_properties(request):
    """Function which calculates the averages of the ratings
    from all the reviews for each property. The results are
    then returned as a context and able to be accessed in all
    HTML files"""
    queryset = Property.objects.filter(status=1)
    for item in queryset:
        reviews = item.reviews.order_by('date_reviewed')
        item.review_count = reviews.all().count()
        item.average_property_rating = reviews.aggregate(Avg('overall_rating'))
        item.average_condition = reviews.aggregate(Avg(
            'condition_of_property'
            ))
        item.landlord_quality = reviews.aggregate(Avg('quality_of_landlord'))
        item.rate_neighbourhood = reviews.aggregate(Avg(
            'rate_the_neighbourhood'
            ))
        item.value_for_money = reviews.aggregate(Avg('value_for_money'))
        item.nearby_amenities = reviews.aggregate(Avg(
            'standard_of_amenities_nearby'
            ))

    context = {
        'properties': queryset
    }

    return context
