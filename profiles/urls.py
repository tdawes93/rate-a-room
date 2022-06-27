from django.urls import path
from . import views as auth_views

urlpatterns = [
    path('login_user/', auth_views.LoginUserView.as_view(), name='login'),
    path('logout_user/', auth_views.logout_user, name='logout'),
    path('register_user/', auth_views.RegisterUser.as_view(), name='register'),

]
