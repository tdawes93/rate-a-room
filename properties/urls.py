from django.urls import path, include
from . import views

urlpatterns = [
    path(
        'add-property/',
        views.PropertyCreateView.as_view(),
        name='add_property'
        ),
    path('summernote/', include('django_summernote.urls')),
    path(
        '<slug:slug>/',
        views.PropertyDetail.as_view(),
        name='property_detail'
        ),
    path(
        'like/<slug:slug>',
        views.PropertyLike.as_view(),
        name='property_like'
        ),
    path(
        'edit-property/<slug:slug>/',
        views.PropertyUpdateView.as_view(),
        name='edit_property',
        ),
]
