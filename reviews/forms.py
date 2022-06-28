from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML, Field, Div
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form class representing the fields of the
    review model are needed to be displayed in the form
    """
    class Meta:
        model = Review
        fields = (
            'title',
            'content',
            'condition_of_property',
            'quality_of_landlord',
            'rate_the_neighbourhood',
            'value_for_money',
            'standard_of_amenities_nearby',
            'date_rented_from',
            'date_rented_to',
        )

    date_rented_from = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date'}
        ))
    date_rented_to = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date'}
        ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['date_rented_from'].label = ''
        self.fields['date_rented_to'].label = ''
        self.fields['condition_of_property'].widget.attrs.update(max='5')
        self.fields['quality_of_landlord'].widget.attrs.update(max='5')
        self.fields['rate_the_neighbourhood'].widget.attrs.update(max='5')
        self.fields['value_for_money'].widget.attrs.update(max='5')
        self.fields['standard_of_amenities_nearby'].widget.attrs.update(max='5')
        self.helper.form_id = 'addreview-form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Div(
                    HTML(
                        '<h4>Give your review a name!</h4>'
                    ),
                    css_class="col",
                ), css_class="row m-2",
            ),
            Div(
                Div(
                    Field('title',),
                    css_class="col",
                ), css_class="row mx-2"
            ),
            Div(
                Div(
                    Field('content',),
                    css_class="col",
                ), css_class="row m-2"
            ),
            Div(
                Div(
                    HTML(
                        '<h4>When did you rent this property?</h4>'
                    ),
                    css_class="col mt-2",
                ), css_class="row m-2",
            ),
            Div(
                Div(
                    HTML(
                        '<h4>from:</h4>'
                    ),
                    css_class="col-2 text-end px-0",
                ),
                Div(
                    Field('date_rented_from',),
                    css_class="col-4",
                ),
                Div(
                    HTML(
                        '<h4>to:</h4>'
                    ),
                    css_class="col-2 text-end",
                ),
                Div(
                    Field('date_rented_to',),
                    css_class="col-4",
                ), css_class="row mx-2 justify-content-left"
            ),
            Div(
                Div(
                    HTML(
                        '<h4>Rate the following aspects of the property'
                        ' between 1 and 5</h4>'
                    ),
                    css_class="col",
                ), css_class="row m-2",
            ),
            Div(
                Div(
                    Fieldset(
                        '',
                        'condition_of_property',
                        'quality_of_landlord',
                        'rate_the_neighbourhood',
                        'value_for_money',
                        'standard_of_amenities_nearby',
                        ), css_class="col"
                ), css_class="row m-2"
            ),
            Div(
                Div(
                    Submit('', 'Save Review', css_class='nav-btn'),
                    css_class="col mt-2 text-center justify-content-center"),
                css_class="row m-2",
            ),
        )
