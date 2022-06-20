from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', views.homepage, name='homepage'),
    path('properties/', include('properties.urls'), name='property_urls'),
]
