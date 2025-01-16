from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'national_code',
            'birth_date',
            'username',
            'password1',
            'password2',
            'mobile',
            'phone',
            'postal_code',
            'email',
            'use_2fa',
            'avatar',
        )