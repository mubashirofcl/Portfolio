from django import forms
from .models import Contact_page



class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact_page
        fields = '__all__'