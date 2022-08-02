from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from properties.models import Property
from .forms import ReviewForm
from .models import Review


class ReviewCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    A standard view class rendering the add review
    page for each review
    """
    model = Review
    template_name = 'add-review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('homepage')
    success_message = 'Your review was created successfully'

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


class ReviewUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    A standard view class rendering the edit review
    page for each review
    """
    model = Review
    template_name = 'edit-review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('homepage')
    success_message = 'Your review was updated successfully'


class ReviewDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    A standard view class rendering the add review
    page for each review using the form_class attribute
    """
    model = Review
    template_name = 'review_confirm_delete.html'
    success_url = reverse_lazy('homepage')
    success_message = 'Your review was deleted successfully'
