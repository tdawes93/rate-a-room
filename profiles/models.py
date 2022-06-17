from django.db import models


# class Profile(models.Model):
#     """
#     A class to represent a user profile able to post properties
#     or write reviews
#     """
#     username = models.CharField(max_length=30, unique=True)
#     firstname = models.CharField(max_length=30)
#     lastname = models.CharField(max_length=30)
#     email = models.EmailField(
#         verbose_name='email address', unique=True
#         )
#     is_ll_or_ea = models.BooleanField(default=False)

#     def __str__(self):
#         return self.username
