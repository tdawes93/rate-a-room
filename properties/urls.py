from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PropertyList.as_view(), name="properties_list"),
    path('summernote/', include('django_summernote.urls')),
]
