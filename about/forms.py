from django import forms
from .models import CollaborateRequest

class CollaborateForm(forms.ModelForm):
    """ 
    Form for handling collaboration/contact requests.
    """
    class Meta:
        """
        Specifies the model to be used and the included fields.
        """
        model = CollaborateRequest
        fields = ('name', 'email', 'message')