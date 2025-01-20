from django.db import models
from django.conf import settings
import random


def generate_random_number():
    return random.randint(100000000, 999999999)


class BusinessCard(models.Model):
    STATUS_CHOISES = {
        'FC': 'تایید نهایی'  # Final Confirmation
    }
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name='کاربر', on_delete=models.CASCADE)
    request_number = models.PositiveIntegerField(
        'شماره درخواست', default=generate_random_number)
    request_type = models.CharField(
        'نوع درخواست', max_length=50, default='صدور')
    created_at = models.DateTimeField('زمان ارسال', auto_now_add=True)
    status = models.CharField('وضعیت', max_length=5,
                              choices=STATUS_CHOISES, default='FC')

    class Meta:
        verbose_name = "کارت بازرگانی"
        verbose_name_plural = "کارت‌های بازرگانی"

    def __str__(self):
        return f'درخواست صدور کارت بازرگانی با شماره {self.request_number} برای {self.user}'
