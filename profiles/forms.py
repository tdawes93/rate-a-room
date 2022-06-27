from django import forms


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

