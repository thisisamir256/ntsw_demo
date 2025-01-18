from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, VerificationCode
import re
from django.core.exceptions import ValidationError


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
        self.fields["username"].widget.attrs["readonly"] = True
        self.fields['password1'].required = True
        self.fields['password2'].required = True
    
    
    def clean_birthday(self):
        data = self.cleaned_data.get('birthday')
        print('birthday is: ', data)
        r = '\d{2,4}\/\d{1,2}\/\d{1,2}'
        print('result is: ', re.search(r,data))
        if not re.search(r,data):
            raise ValidationError("فرمت تاریخ تولد اشتباه است. فرمت تاریخ باید به صورت YYYY/MM/DD باشد.")        
        return data


class UsernameForm(forms.Form):
    username = forms.CharField(max_length=10, min_length=10, label="نام کاربری (کد ملی)")


class PasswordResetForm(forms.Form):
    username = forms.CharField(max_length=10, min_length=10, label="نام کاربری (کد ملی)")
    code = forms.CharField(max_length=4, label="کد تأیید")
    new_password = forms.CharField(widget=forms.PasswordInput, label="رمز عبور جدید")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="تکرار رمز عبور")

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password != confirm_password:
            raise forms.ValidationError("رمز عبور و تکرار آن مطابقت ندارند.")
        return cleaned_data
