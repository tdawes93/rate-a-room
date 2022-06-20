from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    An admin class for the Review model
    """
    prepopulated_fields = {'slug': ('title', 'user')}
    search_fields = ('title', 'property',)
    list_display = ('title', 'property', 'user', 'overall_rating',)
    readonly_fields = ('overall_rating',)
