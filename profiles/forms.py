from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class LoginForm(forms.Form):
    """This form class creates the user login form
    rendered in the profiles.views.py file and displayed in login.html
    """
    username = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )
    email = forms.EmailField(required=False)
    password = forms.CharField(
        min_length=8,
        max_length=60,
        widget=forms.PasswordInput()
    )


class RegisterUserForm(UserCreationForm):
    """
    Class that creates the registration form from
    the User model
    """
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'role',)

        widgets = {
            'role': forms.RadioSelect,
        }


class EditUserForm(UserChangeForm):
    """
    Class that creates the registration form from
    the User model
    """
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            )
