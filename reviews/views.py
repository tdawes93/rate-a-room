from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from properties.models import Property
from .forms import ReviewForm


class ReviewFormView(View):
    """
    A standard view class rendering the add review
    page for each review using the form_class attribute
    """
    form_class = ReviewForm
    initial = {'key': 'value'}
    template_name = 'add-review.html'
    


    def get(self, request, *args, **kwargs):
        """
        This method gets the empty form views from
        the dataset to be filled in by the user
        """
        form = self.form_class(initial=self.initial)
        # if 'slug' in request.POST:
        #     slug = request.POST['slug']
        #     return slug
        slug = request.GET.get("slug")
        queryset = Property.objects.filter(status=1)
        property = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            self.template_name,
            {
                'property': property,
                'slug': slug
            },
        )

    def post(self, request, *args, **kwargs):
        """
        This method posts the individual review information
        from the form back to the dataset
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/properties/<slug:slug>//')

        return render(
            request,
            self.template_name,
            {
                'form': form
            },
            )
