from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    An admin class for the Review model
    """
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
