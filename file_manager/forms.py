from django import forms
from .models import DocumentedInformation


class DocumentedInformationForm(forms.ModelForm):

    class Meta:
        model = DocumentedInformation
        exclude = ('approved',)
