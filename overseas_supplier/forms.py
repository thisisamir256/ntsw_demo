from django import forms

from .models import Person, Company


class PersonCreationForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = (
            'first_name',
            'last_name',
            'father_name',
            'mother_name',
            'grandfather_name',
            'country',
            'city',
            'sex',
            'birthday',
            'nationality',
            'maried',
            'personal_image',
            'document_type',
            'document_number',
            'issue_date',
            'expire_date',
        )
