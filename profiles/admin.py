from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    An admin class for the User model
    """
    search_fields = ('username',)
    list_display = ('username', 'email')
    readonly_fields = ('username',)
