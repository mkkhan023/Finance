from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    contact_no = forms.IntegerField()
    email = forms.EmailField()
    verify_email = forms.EmailField()
    # docs = forms.ImageField()

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Make Sure emails match')

            