from django.db import models

from django.contrib.auth.models import AbstractUser

from django.core.validators import RegexValidator

from django.core.exceptions import ValidationError


class CustomUser(AbstractUser):
    objects = jmodels.jManager()
    national_code = models.CharField('کد ملی', max_length=10)
    birth_date = models.DateField('تاریخ تولد')
    mobile = models.CharField(
        'تلفن همراه',
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
        'تایید موبایل', default=False)
    phone = models.CharField('شماره تلفن',max_length=11)
    postal_code = models.CharField('کد پستی', max_length=10)
    use_2fa = models.BooleanField('مایل به استفاده از رمز دو عاملی هستم', default= False)
    avatar = models.ImageField('تصویر پرسنلی', upload_to='uploads/users/avatar', max_length=100, blank=True, default=None)
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'

    def __str__(self):
        return self.username    
    
    def clean(self):
        if len(self.mobile) != 11:
            raise ValidationError("طول این فیلد باید دقیقاً ۱۱ کاراکتر باشد.")