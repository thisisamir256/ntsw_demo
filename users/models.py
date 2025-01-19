from django.contrib.auth.models import User  # یا مدل کاربر سفارشی شما
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.utils import timezone

from datetime import timedelta, datetime
from decouple import config
import uuid


class CustomUser(AbstractUser):
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
    phone = models.CharField('شماره تلفن', max_length=11)
    postal_code = models.CharField('کد پستی', max_length=10)
    use_2fa = models.BooleanField(
        'مایل به استفاده از رمز دو عاملی هستم', default=False)
    avatar = models.ImageField(
        'تصویر پرسنلی', upload_to='uploads/users/avatar', max_length=100, blank=True, default=None)
    uuid = models.UUIDField('uuid کد', default=uuid.uuid4,
                            editable=False, unique=True)
    base = models.BooleanField('پایه حقیقی/حقوقی', default=True)
    has_business_card = models.BooleanField(
        'بازرگان حقیقی/ حقوقی', default=False)
    has_internal_trader = models.BooleanField(
        'تاجر حقیقی/ حقوقی', default=False)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'

    def __str__(self):
        return self.username

    def clean(self):
        if len(self.mobile) != 11:
            raise ValidationError("طول این فیلد باید دقیقاً ۱۱ کاراکتر باشد.")


class VerificationCode(models.Model):
    user = models.ForeignKey(
        CustomUser, verbose_name='کاربر', on_delete=models.CASCADE)
    uuid = models.UUIDField('uuid کد', default=uuid.uuid4,
                            editable=False, unique=True)
    created_at = models.DateTimeField('ایجاد شده در', auto_now_add=True)
    verification_code = models.PositiveSmallIntegerField(
        'کد تایید',
        validators=[MinValueValidator(1000), MaxValueValidator(9999)]
    )

    class Meta:
        verbose_name = 'کد تایید'
        verbose_name_plural = 'کدهای تایید'
        indexes = [
            models.Index(fields=['user', 'verification_code']),
        ]

    def __str__(self):
        return f'کد {self.verification_code} برای کاربر {self.user} ایجاد شد'

    @property
    def is_valid(self):
        time_turtling = config('SMS_TIME_TURTLING', cast=int, default=3)
        return self.created_at + timedelta(seconds=time_turtling) > timezone.now()
