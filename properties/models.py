from django.db import models

# Create your models here.


class Property(models.Model):
    """
    A class to represnt a property eligible for review.
    """
    title = models.CharField(max_length=100)
