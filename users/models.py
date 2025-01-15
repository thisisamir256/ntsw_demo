from django.db import models
from django.contrib.auth import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class CustomUser(AbstractUser):
    national_code = models.CharField('کد ملی', max_length=10, required=True)
    birth_date = models.DateField('تاریخ تولید')
    mobile = models.CharField(
        _("mobile"),
        max_length=11,
        unique=True,
        blank=False,
        null=False,        
        validators=[
            RegexValidator(
                regex=r'^\d{11}$',  # فقط اعداد و دقیقاً ۱۱ رقم
                message="این فیلد باید دقیقاً شامل ۱۱ رقم باشد.",
            )
        ],
        help_text="این فیلد باید دقیقاً ۱۱ کاراکتر باشد.")
    is_mobile_verified = models.BooleanField(
        _("mobile verified"), default=False)
    phone = models.PhoneNumberField('شماره تلفن')
    postal_code = models.CharField('کد پستی', max_length=10)
    use_2fa = models.BooleanField('استفاده از رمز دو عاملی', default= False)
    avatar = models.FileField('تصویر پرسنلی', upload_to='uploads/users/avatar', max_length=100)
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.username    
    
    def clean(self):
        if len(self.mobile) != 11:
            raise ValidationError("طول این فیلد باید دقیقاً ۱۱ کاراکتر باشد.")