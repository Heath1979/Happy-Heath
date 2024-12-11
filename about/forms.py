from django import forms
from .models import ContactUs


class ContactForm(forms.ModelForm):
    """
    Form for handling collaboration/contact requests.
    """
    class Meta:
        """
        Specifies the model to be used and the included fields.
        """
        model = ContactUs
        fields = ('name', 'email', 'message')
