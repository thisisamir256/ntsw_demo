from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class RegisterForm(UserCreationForm):
    birthday = forms.CharField(label='تاریخ تولد')
    class Meta:
        model = CustomUser
        fields = (
            'national_code',
            'birthday',
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].disabled = True
        self.fields["username"].widget.attrs["readonly"] = True
        self.fields['password1'].required = True
        self.fields['password2'].required = True
