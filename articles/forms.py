from django import forms
from django.forms.widgets import TextInput
from django.utils.translation import gettext_lazy as _
from articles.models import NewsLetter


class NewsLetterForm(forms.ModelForm):

    class Meta:
        model = NewsLetter
        fields = '__all__'
        widgets = {
            'email': TextInput(attrs={'class': 'form-control required', 'placeholder': 'Enter Your Email'}),
        }
        error_messages = {
            'email': {
                'required': _("Email field is required"),
            },
        }
