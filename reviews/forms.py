from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form class representing the fields of the
    review model are needed to be displayed in the form
    """
    class Meta:
        model = Review
        fields = (
            'property',
            'title',
            'content',
            'condition_of_property',
            'quality_of_landlord',
            'rate_the_neighbourhood',
            'value_for_money',
            'standard_of_amenities_nearby',
            'images',
            'date_rented_from',
            'date_rented_to',
        )
