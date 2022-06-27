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
    doc
    """
    def post(self, request, *args, **kwargs):
        """
        doc
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
        doc
        """
        return render(
            request,
            'search-properties.html',
            {},
        )


class SearchPropertyForReview(View):
    """
    doc
    """
    model = Property

    def post(self, request, *args, **kwargs):
        """
        doc
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
            'search-properties-for-review.html',
            {
                'searched': searched,
                'searched_properties': searched_properties,
            },
            )

    def get(self, request, *args, **kwargs):
        """
        doc
        """
        return render(
            request,
            'search-properties-for-review.html',
            {},
        )


class SearchForm(View):
    """Doc"""
    def get(self, request, *args, **kwargs):
        """DOC"""
        return render(
                request,
                'search-form.html',
                {},
            )
