from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from address.models import AddressField


class Property(models.Model):
    """
    A class to represnt a property eligible for review.
    """
    # Specifiy choices for dropdown option
    FLAT = '1'
    TERRACE = '2'
    SEMI = '3'
    DETACHED = '4'
    BUNGALOW = '5'
    SHARE = '6'
    HOUSING_CHOICES = [
        (FLAT, 'Flat'),
        (TERRACE, 'Terrace house'),
        (SEMI, 'Semi-detached house'),
        (DETACHED, 'Detached house'),
        (BUNGALOW, 'Bungalow'),
        (SHARE, 'House share'),
    ]
    # Model fields
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    address = AddressField(null=True)
    num_of_bedrooms = models.PositiveIntegerField(null=True, blank=True)
    num_of_bathrooms = models.PositiveIntegerField(null=True, blank=True)
    type_of_property = models.CharField(
        max_length=30,
        choices=HOUSING_CHOICES,
        default=1,
        blank=False
    )
    for_rent = models.BooleanField(default=False)
    # images = CloudinaryField('image')
    # ll_or_ea = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     verbose_name='Landlord/Estate Agent'
    #     )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Class to add Metadata, in this instance the ordering options
        """
        ordering = ['-created_on', 'title']

    def __str__(self):
        return self.title
