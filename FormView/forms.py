import email
from django import forms

class TestForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget = forms.Textarea)
    email = forms.EmailField()