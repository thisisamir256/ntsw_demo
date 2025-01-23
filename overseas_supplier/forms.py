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
            'subject',
            'address',
            'postal_code',
            'phone',
        )

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        # for field_name, field in self.fields.items():
        #     self.fields[field_name].widget.attrs['placeholder'] = field.label
        print(self.fields)
        print(self.fields['company_type'].__dir__())
        self.fields['company_type'].widget.attrs['placeholder'] = 'جستجو کنید'
