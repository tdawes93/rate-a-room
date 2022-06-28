from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    An admin class for the User model
    """
    search_fields = ('username', 'role',)
    list_display = ('username', 'email', 'role',)
    readonly_fields = ('username',)
