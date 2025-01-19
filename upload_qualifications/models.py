from django.db import models
from django.conf import settings


class BusinessCard(models.Model):
    STATUS_CHOISES = {
        'FC': 'تایید نهایی'  # Final Confirmation
    }
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name='کاربر', on_delete=models.CASCADE)
    request_number = models.PositiveIntegerField('شماره درخواست')
    request_type = models.CharField(
        'نوع درخواست', max_length=50, default='صدور')
    created_at = models.DateField('زمان ارسال', auto_now_add=True)
    status = models.CharField('وضعیت', max_length=5,
                              choices=STATUS_CHOISES, default='FC')

    class Meta:
        verbose_name = "کارت بازرگانی"
        verbose_name_plural = "کارت‌های بازرگانی"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("BusinessCard_detail", kwargs={"pk": self.pk})
