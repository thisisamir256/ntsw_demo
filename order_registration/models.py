from django.db import models


class MainData(models.Model):
    # performa_number

    class Meta:
        verbose_name = 'اطلاعات اصلی'
        verbose_name_plural = 'اطلاعات اصلی'

    def __str__(self):
        return self.name
