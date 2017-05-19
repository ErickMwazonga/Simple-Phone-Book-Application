from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, MultiWidgetField, Submit

# A form for the Contact model
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'location', 'emergency_contact']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'required': True, "placeholder": "Enter First Name"}
            ),
            'last_name': forms.TextInput(
                attrs={'required': True, 'placeholder': "Enter Last Name"}
            ),
            'phone_number': forms.NumberInput(
                attrs={'required': True, "placeholder": "Enter Phone Number"}
            ),
            'email': forms.EmailInput(
                attrs={'required': True, 'placeholder': "Enter Email Address"}
            ),
            'location': forms.TextInput(
                attrs={'required': True, "placeholder": "Enter Location"}
            ),
            'emergency_contact': forms.NumberInput(
                attrs={'required': True, 'placeholder': "Enter Emergency Contact Number"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = Contact.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email

class ContactSearchForm(forms.Form):
    # widgets = {
    #     'name': forms.TextInput(
    #         attrs={'id':"search_name"}
    #     )
    #     'phone': forms.IntegerField(
    #         attrs={'id':"search_phone"}
    #     )
    # }
    name = forms.CharField(
        max_length=100,
        required=False,
        help_text='Search by first name or last name'
    )
    phone = forms.IntegerField(
        required=False,
        help_text='Search by first name or last name'
    )


    def __init__(self, *args, **kwargs):
        super(ContactSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            'name',
            'phone',
            Submit('Search', 'search', css_class='btn-default'),
        )
        self.helper.form_method = 'get'

    def get_queryset_filters(self):
        filters = {}
        if self.is_valid():
            name = self.cleaned_data.get('name')
            filters['name'] = name
