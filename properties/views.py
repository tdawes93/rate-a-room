from django.shortcuts import get_object_or_404, render, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from .models import Property
from .forms import PropertyForm


class PropertyCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A standard view class rendering the add property
    page for each review using the form_class attribute
    """
    form_class = PropertyForm
    model = Property
    template_name = 'add-property.html'

    def test_func(self):
        if self.request.user.role == 'LL_OR_EA':
            return True
        else:
            return HttpResponse(
                "You are not authenticated to edit this profile",
                status=403)


class PropertyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A standard view class rendering the edit property
    page for each review using the form_class attribute
    """
    form_class = PropertyForm
    model = Property
    template_name = 'edit-property.html'

    def test_func(self):
        if self.request.user.role == 'LL_OR_EA':
            return True
        else:
            return HttpResponse(
                "You are not authenticated to edit this profile",
                status=403)



class PropertyDetail(View):
    """
    A standard view class rendering the individual
    page for each property
    """

    def get(self, request, slug, *args, **kwargs):
        """
        This method gets the individual property information
        needed for each property page from the model dataset
        """
        queryset = Property.objects.filter(status=1)
        property = get_object_or_404(queryset, slug=slug)
        reviews = property.reviews.order_by('date_reviewed')

        liked = False
        if property.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'property.html',
            {
                'slug': slug,
                'property': property,
                'reviews': reviews,
                'liked': liked,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        This method gets the individual property information
        needed for each property page from the model dataset
        """
        queryset = Property.objects.filter(status=1)
        property = get_object_or_404(queryset, slug=slug)
        reviews = property.reviews.order_by('date_reviewed')

        liked = False
        if property.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'property.html',
            {
                'slug': slug,
                'property': property,
                'reviews': reviews,
                'liked': liked,
            },
        )


class PropertyLike(View):
    """Class view to accept the request to like a
    property. It checks if the property has or hasn't
    been liked by the user and renders the new page
    accordingly"""

    def post(self, request, slug, *args, **kwargs):
        """Post request for generic propertylike view,
        will update the likes field on the property model"""
        property = get_object_or_404(Property, slug=slug)
        if property.likes.filter(id=request.user.id).exists():
            property.likes.remove(request.user)
        else:
            property.likes.add(request.user)

        return HttpResponseRedirect(reverse('property_detail', args=[slug]))
