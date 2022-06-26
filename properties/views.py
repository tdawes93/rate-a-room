from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import View
from .models import Property
from .forms import PropertyForm


class PropertyCreateView(CreateView):
    """
    A standard view class rendering the add property
    page for each review using the form_class attribute
    """
    form_class = PropertyForm
    model = Property
    template_name = 'add-property.html'

    # def get(self, request, *args, **kwargs):
    #     """DOC"""
    #     form = self.form_class()

    #     return render(
    #         request,
    #         self.template_name,
    #         {
    #             'form': form,
    #             'property': property,
    #         }
    #     )



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

        return render(
            request,
            'property.html',
            {
                'slug': slug,
                'property': property,
                'reviews': reviews,
            },
        )
