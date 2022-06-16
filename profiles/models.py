from django.db import models


class Profile(models.Model):
    """
    A class to represent a user profile able to post properties
    or write reviews
    """
    username = models.CharField(max_length=30, unique=True)
