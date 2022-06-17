from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from address.models import AddressField


class Property(models.Model):
    """
    A class to represnt a property eligible for review.
    """
    # Specifiy choices for dropdown option
    CONDITION = '1'
    QUALITY = '2'
    RATE = '3'
    STANDARD = '4'
    VALUE = '5'
    HOUSING_CHOICES = [
        (CONDITION, 'Condition of property'),
        (QUALITY, 'Quality of landlord'),
        (RATE, 'Rate the neighbourhood'),
        (STANDARD, 'Standard of amenities nearby'),
        (VALUE, 'Value for money'),
    ]
    # Model fields
    title = models.CharField(max_length=100)
    address = AddressField(null=True)
    num_of_bedrooms = models.PositiveIntegerField()
    num_of_bathrooms = models.PositiveIntegerField()
    type_of_property = models.CharField(
        max_length=30,
        choices=HOUSING_CHOICES,
        default=1,
        blank=False
    )
    for_rent = models.BooleanField(default=False)
    images = CloudinaryField('image')
    ll_or_ea = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Landlord/Estate Agent'
        )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Class to add Metadata, in this instance the ordering options
        """
        ordering = ['-created_on', 'title']

    def __str__(self):
        return self.title
