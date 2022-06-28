from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Review


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """
    An admin class for the Review model
    """
    summernote_fields = ('content')
    search_fields = ('title', 'property',)
    list_display = ('title', 'property', 'user', 'overall_rating',)
    readonly_fields = ('overall_rating',)
