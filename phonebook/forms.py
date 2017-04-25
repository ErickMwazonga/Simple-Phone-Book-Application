from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper

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
