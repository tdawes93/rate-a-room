from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    """
    Form class representing the fields of the
    review model are needed to be displayed in the form
    """
    class Meta:
        model = Property
        fields = (
            'title',
            'street_address',
            'address_street2',
            'address_town',
            'address_county',
            'address_postcode',
            'address_country',
            'images',
            'num_of_bedrooms',
            'num_of_bathrooms',
            'type_of_property',
            'for_rent',
            'status',
        )

        widgets: {
            
        }
