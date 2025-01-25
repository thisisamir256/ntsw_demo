from django import forms
from .models import MainData


class MainDataForm(forms.ModelForm):

    class Meta:
        model = MainData
        fields = (
            "proforma_invoice",
            'beneficiary_country',
            'proforma_invoice_issue_date',
            'proforam_invoice_expire_date',
            'order_registration_case',
            # 'supplier_type',
            # 'object_id',
            # 'related_object',
            'producer_type',
        )
