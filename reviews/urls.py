from django.urls import path, include
from . import views

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path(
        'add_review/',
        views.ReviewCreateView.as_view(),
        name='add_review'
    ),
    path(
        'edit-review/<int:pk>/',
        views.ReviewUpdateView.as_view(),
        name='edit_review',
    ),
    path(
        'delete_review/<int:pk>/',
        views.ReviewDeleteView.as_view(),
        name='delete_review',
        ),
    ]
