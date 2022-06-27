from django import forms


class LoginForm(forms.Form):
    """Doc"""
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
