from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML, Field, Div
from .models import Property


class PropertyForm(forms.ModelForm):
    """
    Form class representing the fields of the
    review model are needed to be displayed in the form
    """
    class Meta:
        model = Property
        fields = (
            'title',
            'street_address',
            'address_street2',
            'address_town',
            'address_county',
            'address_postcode',
            'address_country',
            'images',
            'num_of_bedrooms',
            'num_of_bathrooms',
            'type_of_property',
            'for_rent',
            'status',
        )

        widgets = {
            'type_of_property': forms.RadioSelect,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['images'].label = ''
        self.helper = FormHelper()
        self.helper.form_id = 'addproperty-form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                HTML(
                    '<div class="col">'
                    '<h4>Please name this property so it can stand out!</h4>'
                    '</div>',
                    ),
                css_class="row m-2"
            ),
            Div(
                Div(Field('title',), css_class="col"), css_class="row m-2"),
            Div(
                HTML(
                    '<div class="col mt-2">'
                    '<h4>Add your property details below:</h4>'
                    '</div>',
                    ),
                css_class="row m-2"
            ),
            Div(
                Div(
                    Fieldset(
                        '',
                        'type_of_property',
                        'num_of_bedrooms',
                        'num_of_bathrooms',),
                    css_class="col"),
                css_class="row m-2"
            ),
            Div(
                HTML(
                    '<div class="col mt-2">'
                    '<h4>How can we find this place?</h4>'
                    '</div>',
                    ),
                css_class="row m-2"
                ),
            Div(
                Div(
                    Fieldset(
                        '',
                        'street_address',
                        'address_street2',
                        'address_town',
                        'address_county',
                        'address_postcode',
                        'address_country',),
                    css_class="col"),
                css_class="row m-2"
            ),
            Div(
                HTML(
                    '<div class="col mt-2">'
                    '<h4>Is this property currently listed as "To Let"?</h4>'
                    '</div>',
                    ),
                css_class="row m-2"),
            Div(
                Div(
                    Field('for_rent',),
                    css_class="col"),
                css_class="row m-2",
            ),
            Div(
                HTML(
                    '<div class="col mt-2">'
                    '<h4>Add any images of your property!</h4>'
                    '</div>',
                    ),
                css_class="row m-2"),
            Div(
                Div(
                    Field('images'),
                    css_class="col"),
                css_class="row m-2",
            ),
            Div(
                HTML(
                    '<div class="col mt-2">'
                    '<h4>Please select the status of the post for this'
                    ' property</h4>'
                    '<h6>If you wish to save a draft copy to return to later'
                    ', please select "draft" and then "submit".'
                    ' The property will be added to your account but hidden'
                    ' for other users<h6></div>',
                    ),
                css_class="row m-2"),
            Div(
                Div(
                    Field('status',),
                    css_class="col"),
                css_class="row m-2",
            ),
            Div(
                Div(
                    Submit('', 'Add Property', css_class='nav-btn'),
                    css_class="col mt-2 text-center justify-content-center"),
                css_class="row m-2",
            ),
        )
