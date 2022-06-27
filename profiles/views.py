from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from . import forms


class LoginUserView(View):
    """Generic view that takes the Login Form and
    renders it. In event of a Post request the login
    details are authenticated and a new page is rendered or
    the page is reloaded"""
    form_class = forms.LoginForm
    template_name = 'authenticate/login.html'

    def get(self, request):
        """Get request for the Login user view. It takes
        the login form and renders it on the html page. No
        message is shown"""
        form = self.form_class()
        message = ''
        return render(
            request,
            self.template_name,
            {
              'form': form,
              'message': message,
            }
        )

    def post(self, request):
        """Post request for Login view. The login form is validated and if
        passed the login info is authenticated. In the event of an authorised
        user the user is logged in and redirected to the homepage. If a fail
        occurs the page is reloaded"""
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'You are loggin in as {user.username}'
                return redirect('homepage')

        message = 'Login failed!'
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'message': message
            }
        )


def logout_user(request):
    logout(request)
    return redirect('homepage')
