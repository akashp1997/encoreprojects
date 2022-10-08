from django import forms
from django.utils.timezone import now


class ProjectForm(forms.Form):
    po_code = forms.IntegerField(
        label='PO Code',
        min_value=0,
        error_messages={
            'required': 'Please enter PO #',
            'invalid': 'Please enter a valid PO #',
            'min_value': 'PO # has to be greater than 0'
        }
    )
    name = forms.CharField(
        label='Project Name',
        max_length=256,
        error_messages={
            'required': 'Please enter the project name',
            'max_length': 'The project name cannot be longer than 255 characters'
        }
    )
    description = forms.CharField(
        label='Spec description',
        error_messages={
            'required': 'Please enter the spec description'
        },
        widget=forms.Textarea
    )
    po_date = forms.DateField(
        label='PO Date',
        initial=now(),
        error_messages={
            'required': 'Please enter the PO Date'
        }
    )
    po_spec = forms.CharField(
        label='Main PO spec',
        max_length=256,
        error_messages={
            'required': 'Please enter the Main PO Spec',
            'max_length': 'The main PO spec cannot be longer than 255 characters'
        }
    )
    supplier_name = forms.CharField(
        label='Supplier name',
        max_length=256,
        error_messages={
            'required': 'Please enter the supplier name',
            'max_length': 'The supplier name cannot be longer than 255 characters'
        }
    )
