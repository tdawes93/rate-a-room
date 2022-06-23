from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from cloudinary.models import CloudinaryField
from properties.models import Property


# def date_validation(date1, date2):
#     """
#     A validator function to check the date_rented_from
#     occurs before the date_rented_to
#     """
#     if


class Review(models.Model):
    """
    A class to represent the reviews for each proeprty
    """
    # Model fields
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    date_rented_from = models.DateField(null=True, blank=True)
    date_rented_to = models.DateField(null=True, blank=True)
    content = models.TextField(max_length=500, null=True, blank=True)
    condition_of_property = models.PositiveIntegerField(
        validators=[MaxValueValidator(5),],
        default=0,
    )
    quality_of_landlord = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)],
        default=0,
    )
    rate_the_neighbourhood = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)],
        default=0,
    )
    value_for_money = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)],
        default=0,
    )
    standard_of_amenities_nearby = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)],
        default=0,
    )
    overall_rating = models.PositiveIntegerField(blank=True, null=True)
    date_reviewed = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='reviews')
    likes = models.ManyToManyField(
        User,
        related_name='review_likes',
        blank=True,
    )
    images = CloudinaryField(
        'image',
        default='placeholder',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.title} by {self.user}'

    def save(self, *args, **kwargs):
        self.overall_rating = int(sum(
            [
                self.condition_of_property,
                self.quality_of_landlord,
                self.rate_the_neighbourhood,
                self.value_for_money,
                self.standard_of_amenities_nearby
            ]
        )) / 5
        return super(Review, self).save(*args, **kwargs)

    def snippet(self):
        return self.content[:100] + '...'

    def num_of_likes(self):
        return self.likes.count()
