from django import forms

from .models import Person, Company

class PersonCreationForm(forms.ModelForm):
    
    class Meta:
        model = Person
        fields = (
            
        )
