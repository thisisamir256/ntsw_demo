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


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = (
            'name',
            'en_name',
            'register_number',
            'company_type',
            'registered_country',
            'registered_date',
            'registered_from',
            'owner_type',
            'country',
            'city',
            'address',
            'postal_code',
            'phone',
        )
