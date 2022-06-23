from django.urls import path, include
from . import views

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('add_a_review/', views.ReviewFormView.as_view(), name='add_review'),
]
