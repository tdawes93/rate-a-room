from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


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
    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default='Tenant'
        )

    def get_absolute_url(self):
        return reverse('edit_user', kwargs={'pk': self.pk})
