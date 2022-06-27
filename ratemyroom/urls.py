from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', views.PropertyList.as_view(), name='homepage'),
    path('properties/', include('properties.urls'), name='property_urls'),
    path('reviews/', include('reviews.urls'), name='review_urls'),
    path(
        'profiles/',
        include('django.contrib.auth.urls'),
        name='django_auth_urls'
        ),
    path('profiles/', include('profiles.urls'), name='profiles_urls'),
    path(
        'search_properties/',
        views.SearchProperty.as_view(),
        name='search_properties'
    ),
    path(
        'search_properties_for_review/',
        views.SearchPropertyForReview.as_view(),
        name='search_properties_for_review'
    ),
    path('search_form', views.SearchForm.as_view(), name='search_form')
]

urlpatterns += staticfiles_urlpatterns()
