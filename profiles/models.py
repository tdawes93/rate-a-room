from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary import CloudinaryImage


class User(AbstractUser):
    """
    A class to represent a user profile able to post properties
    or write reviews
    """
    LL_OR_EA = 'LANDLORD_OR_ESTATEAGENT'
    TENANT = 'TENANT'
  
    ROLE_CHOICES = (
        (LL_OR_EA, 'Landlord or Estate Agent'),
        (TENANT, 'Tenant'),
    )
    profile_photo = CloudinaryImage()
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username
