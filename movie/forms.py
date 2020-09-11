from django.forms import ModelForm
from django import forms

from .models import Customer

class CreateCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'contact_no']

class CreateContactForm(forms.Form):
    contact_no = forms.CharField(label='contact_no', max_length=10)
