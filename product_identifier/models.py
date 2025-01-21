from django.db import models


class ProductCategory(models.Model):
    title = models.CharField('عنوان', max_length=100)
    description = models.CharField('توضیح', max_length=250)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی'

    def __str__(self):
        return f'دسته بندی‌ {self.title}'


class Product(models.Model):
    title = models.CharField('عنوان سرفصل', max_length=250)
    en_title = models.CharField('کتگوری', max_length=250)
    featue_image = models.ImageField(
        'تصویر کالا', upload_to='uploads/product_identifier', max_length=500)
    description = models.TextField('تعریف سرفصل')
    message = models.TextField('هشدار')
    code = models.PositiveSmallIntegerField('کد سرفصل')
    gtin = models.JSONField('شناسه جهانی کالا(GTIN)')
    hs = models.JSONField('کد HS')
    isic = models.JSONField('کد ISIC')
    count_unit = models.JSONField('واحد شمارش')
    mandatory_descriptive_field = models.JSONField('فیلدهای توصیفی اجباری')
    optional_fields = models.JSONField('فیلدهای اختیاری')

    class Meta:
        verbose_name = 'کالا'
        verbose_name_plural = 'کالا'

    def __str__(self):
        return self.title
