from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from properties.models import Property
from .forms import ReviewForm
from .models import Review


class ReviewCreateView(View):
    """
    A standard view class rendering the add review
    page for each review using the form_class attribute
    """
    form_class = ReviewForm
    model = Review
    template_name = 'add-review.html'

    def get(self, request, *args, **kwargs):
        """
        This method gets the empty form views from
        the dataset to be filled in by the user
        """
        slug = request.GET.get("slug")
        queryset = Property.objects.filter(status=1)
        property = get_object_or_404(queryset, slug=slug)

        initial = {'property': property}
        form = self.form_class(initial=initial)

        return render(
            request,
            self.template_name,
            {
                'slug': slug,
                'form': form,
                'property': property,
            },
        )

    # def post(self, id, request, *args, **kwargs):
    #     """
    #     This method handles the post request and saves the review information
    #     from the form  to the dataset
    #     """
    #     rate = Review.objects.get(id=id)
    #     form = self.form_class(request.POST)
    #     if request.POST.get('save'):
    #         for field in rate:
    #             field.save()

    #     if form.is_valid():
    #         form.save()
    #         text = form.cleaned_data[
    #             'property',
    #             'title',
    #             'content',
    #             'condition_of_property',
    #             'quality_of_landlord',
    #             'rate_the_neighbourhood',
    #             'value_for_money',
    #             'standard_of_amenities_nearby',
    #             'images',
    #             'date_rented_from',
    #             'date_rented_to'
    #             ]
    #         return HttpResponseRedirect('/properties/<slug:slug>//')

    #     return render(
    #         request,
    #         self.template_name,
    #         {
    #             'form': form,
    #             'text': text
    #         },
    #         )
