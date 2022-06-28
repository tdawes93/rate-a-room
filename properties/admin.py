from django.contrib import admin
from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    """
    An admin class for the property model
    """
    prepopulated_fields = {'slug': ('title', 'address_postcode')}
    search_fields = ('title', 'address_postcode')
    list_display = (
        'title',
        'street_address',
        'address_postcode',
        'num_of_bedrooms',
        'for_rent',
        'll_or_ea',
    )
