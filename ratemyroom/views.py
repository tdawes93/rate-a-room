from django.shortcuts import render
from django.db.models import Q
from django.views import generic, View
from properties.models import Property


class PropertyList(generic.ListView):
    """
    A list view class rendering the properties main page
    """
    model = Property
    queryset = Property.objects.filter(status=1)
    template_name = 'index.html'


class SearchProperty(View):
    """
    A generic view class rendering the search page
    """
    def post(self, request, *args, **kwargs):
        """
        Post request for the search page, the property
        objects are filtered by critera allowing the user
        to search for different address types
        """
        searched = request.POST.get('searched')
        searched_properties = Property.objects.filter(Q(
            address_postcode__icontains=searched)
            | Q(address_town__icontains=searched)
            | Q(address_county__icontains=searched)
            | Q(address_country__icontains=searched)
            )
        return render(
            request,
            'search-properties.html',
            {
                'searched': searched,
                'searched_properties': searched_properties,
            },
            )

    def get(self, request, *args, **kwargs):
        """
        The get request for the search page rendering
        the basic template
        """
        return render(
            request,
            'search-properties.html',
            {},
        )


class SearchPropertyForReview(View):
    """
    Generic class view rending the same search page,
    the links then take you to the add-review page
    """
    model = Property

    def post(self, request, *args, **kwargs):
        """
        Post request for the search page, the property
        objects are filtered by critera allowing the user
        to search for different address types        """
        searched = request.POST.get('searched')
        searched_properties = Property.objects.filter(Q(
            address_postcode__icontains=searched)
            | Q(address_town__icontains=searched)
            | Q(address_county__icontains=searched)
            | Q(address_country__icontains=searched)
            )
        return render(
            request,
            'search-properties-for-review.html',
            {
                'searched': searched,
                'searched_properties': searched_properties,
            },
            )

    def get(self, request, *args, **kwargs):
        """
        The get request for the search page rendering
        the basic template
        """
        return render(
            request,
            'search-properties-for-review.html',
            {},
        )


class SearchForm(View):
    """
    A generic view rending the search bar itself
    """
    def get(self, request, *args, **kwargs):
        """
        Get request for the search bar
        """
        return render(
                request,
                'search-form.html',
                {},
            )
