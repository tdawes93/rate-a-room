from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import View, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from properties.models import Property
from reviews.models import Review
from .models import User
from . import forms
from .forms import RegisterUserForm, EditUserForm


class LoginUserView(View):
    """Generic view that takes the Login Form and
    renders it. In event of a Post request the login
    details are authenticated and a new page is rendered or
    the page is reloaded"""
    form_class = forms.LoginForm
    template_name = 'authenticate/login.html'
    http_method_names = ['get', 'post']

    def get(self, request):
        """Get request for the Login user view. It takes
        the login form and renders it on the html page. No
        message is shown"""
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
              'form': form,
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
                messages.success(
                    request,
                    f'You are logged in as {user.username}'
                    )
                return redirect('homepage')

        messages.success(request, 'Login failed!')
        return render(
            request,
            self.template_name,
            {
                'form': form,
            }
        )


def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully logged out')

    return redirect('homepage')


class RegisterUser(SuccessMessageMixin, CreateView):
    """
    Class view to render a form to allow users
    to register with the site, the post request
    then takes their info and makes an instance of
    the Custom User model so they can log in and
    use the other features on the site
    """
    template_name = 'authenticate/register_user.html'
    form_class = RegisterUserForm
    model = User
    success_url = reverse_lazy('homepage')
    success_message = "Registration successful!"

    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return to_return


class EditUser(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """
    A standard view class rendering the user profile
    page
    """
    template_name = 'authenticate/edit_profile.html'
    form_class = EditUserForm
    model = User
    success_url = reverse_lazy('homepage')
    success_message = "Profile succesfully updated!"

    def get(self, request, *args, **kwargs):
        properties = Property.objects.all()
        reviews = Review.objects.all()
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
              'form': form,
              'reviews': reviews,
              'properties': properties
            }
        )


class DeleteUser(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    A standard view class deleting the property
    before redirecting to the homepage
    """
    model = User
    template_name = 'authenticate/profile_confirm_delete.html'
    success_url = reverse_lazy('homepage')
    success_message = 'Your profile has been deleted succesfully!'


class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    """
    Custom class view to change the password of users
    upon request
    """
    form_class = PasswordChangeForm
    template_name = 'authenticate/change-password.html'
    success_url = reverse_lazy('homepage')
    success_message = "Password changed succesfully!"
