from django import forms

from .models import Person, Company


class PersonCreationForm(forms.ModelForm):
    gender = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=Person.GENDER_CHOISES
    )

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
            'gender',
            'birthday',
            'nationality',
            'maried',
            'personal_image',
            'document_type',
            'document_number',
            'issue_date',
            'expire_date',
        )
