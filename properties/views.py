from django.views import generic
from .models import Property


class PropertyList(generic.ListView):
    """
    A list view class rendering the properties main page
    """
    model = Property
    queryset = Property.objects.filter(status=1).order_by(
        '-created_on',
        'title',
    )
    template_name = 'properties.html'
    paginate_by = 4
