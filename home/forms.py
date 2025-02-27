from django import forms
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nume', 'autocomplete': 'name'}),
                           validators=[RegexValidator(r'^[0-9a-zA-Z ]*$', message='Name must be alphanumeric.')], label='Name', required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={ 'placeholder': 'Email', 'autocomplete': 'email'}), label='Email', required=True)
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'placeholder': 'Subiect', 'autocomplete': 'subject'}), label='Subject', required=True)
    
    message = forms.CharField(widget=forms.Textarea(attrs={ 'placeholder':'Mesajul tau'}), label='Message', required=True)
   

    def clean_message(self):
        message = self.cleaned_data['message']
        # Basic cleanup to escape potentially malicious characters
        sanitized_message = mark_safe(message)
        return sanitized_message



