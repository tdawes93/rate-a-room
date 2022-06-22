from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AddProperty.as_view(), name='properties_list'),
    path('summernote/', include('django_summernote.urls')),
    path(
        '<slug:slug>/',
        views.PropertyDetail.as_view(),
        name='property_detail'
        ),
]
