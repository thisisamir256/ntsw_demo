from django import forms
from .models import MainData
from overseas_supplier.models import Person, Company


class MainDataForm(forms.ModelForm):
    choices = [
        ('person', 'حقیقی'),
        ('company', 'حقوقی')
    ]
    related_object_id = forms.IntegerField()

    class Meta:
        model = MainData
        fields = (
            "proforma_invoice",
            'beneficiary_country',
            'proforma_invoice_issue_date',
            'proforam_invoice_expire_date',
            'order_registration_case',
            'producer_type',
        )

        def save(self, commit=True):
            instance = super.save(commit=False)
            supplier_type = self.cleaned_data['supplier_type']
            object_id = self.cleaned_data['related_object_id']

            if supplier_type == 'person':
                instance.supplier_type = ContentType.objects.get_for_model(
                    Person)
            elif supplier_type == 'company':
                instance.supplier_type = ContentType.objects.get_for_model(
                    Company)
            instance.object_id = object_id

            if commit:
                instance.save()
            return instance
