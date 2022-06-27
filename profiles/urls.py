from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.LoginUserView.as_view(), name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('register_user/', views.RegisterUser.as_view(), name='register'),

]
