from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from properties.models import Property
from .forms import ReviewForm
from .models import Review

class ReviewCreateView(LoginRequiredMixin, View):
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

    def post(self, request, *args, **kwargs):
        """
        This method handles the post request and saves the review information
        from the form  to the dataset
        """
        form = self.form_class(request.POST)

        if form.is_valid():
            text = form.cleaned_data[
                'property',
                'title',
                'content',
                'condition_of_property',
                'quality_of_landlord',
                'rate_the_neighbourhood',
                'value_for_money',
                'standard_of_amenities_nearby',
                'images',
                'date_rented_from',
                'date_rented_to'
                ]
            review = form.save()
            review.save()

            return HttpResponseRedirect(reverse('homepage'))

        return render(
            request,
            self.template_name,
            {
                'form': form,
                'property': property
            },
            )
