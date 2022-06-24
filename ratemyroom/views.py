from django.shortcuts import render
from django.db.models import Q
from django.views import generic, View
from properties.models import Property


class PropertyList(generic.ListView):
    """
    A list view class rendering the properties main page
    """
    model = Property
    queryset = Property.objects.filter(status=1).order_by(
        '-created_on',
        'title',
    )
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
        property = Property.objects.all()
        postcodes = Property.objects.filter(Q(
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
                'postcodes': postcodes,
                'property': property,
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