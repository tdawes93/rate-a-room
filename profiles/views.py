from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import View
from .forms import LoginForm
from . import forms


class LoginUserView(View):
    """Doc"""
    form_class = forms.LoginForm
    template_name = 'authenticate/login.html'

    def get(self, request):
        """Doc"""
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
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
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
