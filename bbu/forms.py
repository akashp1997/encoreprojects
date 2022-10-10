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
        },
        widget=forms.TextInput
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


class BBURowForm(forms.Form):
    po_line_item_no = forms.IntegerField(
        label='PO line item no.',
        min_value=0,
        error_messages={
            'required': 'Please enter the PO line item no.',
            'min_value': 'PO line item no. cannot be less than 0'
        },
        widget=forms.TextInput
    )
    po_position_no = forms.IntegerField(
        label='PO position no.',
        min_value=0,
        error_messages={
            'required': 'Please enter the PO position no.',
            'min_value': 'PO position no. cannot be less than 0'
        },
        widget=forms.TextInput
    )
    erection_item = forms.CharField(
        label='Erection item / KKS / Technocode',
        max_length=256,
        error_messages={
            'required': 'Please enter the erection item info',
            'min_value': 'PO line item no. cannot be less than 0'
        },
        widget=forms.TextInput
    )
    forecast_date = forms.DateField(
        label='Forecast date',
        required=False
    )
    description = forms.CharField(
        label='Description',
        error_messages={
            'required': 'Please enter the item description'
        },
        widget=forms.Textarea,
    )
    quantity = forms.IntegerField(
        label='Required qty',
        initial=1,
        min_value=1,
        error_messages={
            'required': 'Please enter the required quantity',
            'min_value': 'Required quantity must be greater than 0'
        },
        widget=forms.TextInput
    )
    supplier_identification_no = forms.CharField(
        label='Supplier ident. / Part list no. / Part list pos.',
        required=False
    )
