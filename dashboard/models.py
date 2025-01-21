from django.db import models


class Country(models.Model):

    name = models.CharField('نام کشور', max_length=50)

    class Meta:
        verbose_name = 'کشور'
        verbose_name_plural = 'کشور'

    def __str__(self):
        return self.name
