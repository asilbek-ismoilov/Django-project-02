from django.forms import ModelForm
from django import forms
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]

    def clean(self):
        name = self.cleaned_data.get('nmae')
        email = self.cleaned_data.get('nmae')
        message = self.cleaned_data.get('nmae')
        if name:
            if len(name) < 3: 
                self._errors['name'] = self.error_class([ 
                    'Minimum 3 characters required'])
        else:
            self._errors['name'] = self.error_class([
                'name is required'])
            
        if email:
            if len(name) < 5: 
                self._errors['email'] = self.error_class([
                'Email is required'
        ])

        if message:
            if len(name) < 3: 
                self._errors['message'] = self.error_class([
                'Message is required'
        ])