from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', views.PropertyList.as_view(), name='homepage'),
    path('properties/', include('properties.urls'), name='property_urls'),
]

urlpatterns += staticfiles_urlpatterns()