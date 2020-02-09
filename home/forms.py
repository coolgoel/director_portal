from django import forms

from .models import *

class Internal_creation_form(forms.ModelForm):
    class Meta:
        model = internal_letter
        fields =[
        	'si_no',
			'in_date',
			'doc_type',
			'reference',
			'fromm',
			'out_date',
			'to',
			'subject',
			'remarks',
        ]

class External_creation_form(forms.ModelForm):
    class Meta:
        model = external_letter
        fields =[
        	'si_no',
			'receipt_date',
			'fromm',
			'subject',
			'marked_to',
			'action_needed',
			'file',
			'remarks',
        ]

    