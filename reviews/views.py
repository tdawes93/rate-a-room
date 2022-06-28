from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from properties.models import Property
from .forms import ReviewForm
from .models import Review


class ReviewCreateView(LoginRequiredMixin, CreateView):
    """
    A standard view class rendering the add review
    page for each review using the form_class attribute
    """
    model = Review
    template_name = 'add-review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('property_detail')
    success_message = (
        f'Your review of {property}'
        f'was created successfully')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.request.GET.get("slug")
        queryset = Property.objects.filter(status=1)
        property = get_object_or_404(queryset, slug=slug)
        context['property'] = property
        return context

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        print(context)
        form.instance.property = context['property']
        form.instance.user = self.request.user
        form.save()
        return super(ReviewCreateView, self).form_valid(form)


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    """
    A standard view class rendering the add review
    page for each review using the form_class attribute
    """
    model = Review
    template_name = 'edit-review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('homepage')
    success_message = (
        f'Your review of {property}'
        f'was updated successfully')

    # def get(self, request, *args, **kwargs):

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     slug = self.request.GET.get("slug")
    #     queryset = Property.objects.filter(status=1)
    #     property = get_object_or_404(queryset, slug=slug)
    #     context['property'] = property
    #     return context

    # def form_valid(self, form, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     print(context)
    #     form.instance.property = context['property']
    #     form.instance.user = self.request.user
    #     form.save()
    #     return super(ReviewCreateView, self).form_valid(form)
