from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings


class OrderRegistrationCase(models.Model):
    title = models.CharField('عنوان', max_length=50)

    class Meta:
        verbose_name = 'حالت ثبت سفارش'
        verbose_name_plural = 'حالت ثبت سفارش'

    def __str__(self):
        return self.title


class ShippingType(models.Model):
    title = models.CharField('عنوان', max_length=50)

    class Meta:
        verbose_name = "shippingtype"
        verbose_name_plural = "shippingtypes"

    def __str__(self):
        return self.title


class ContractType(models.Model):
    title = models.CharField('عنوان', max_length=50)
    code = models.CharField('کد', max_length=50)
    shipping_type = models.ManyToManyField(
        ShippingType, verbose_name='روش‌های حمل و نقل')

    class Meta:
        verbose_name = 'نوع قرارداد'
        verbose_name_plural = 'نوع قرارداد'

    def __str__(self):
        return self.code


class MainData(models.Model):
    # SUPPLIER_TYPE = {
    #     'p': 'حقیقی',
    #     'c': 'حقوقی',
    # }
    PRODUCER_TYPE = {
        'i': 'صنعتی (بهین یاب)',  # industrial
        'g': 'صنفی',  # guild
        'm': 'معدنی',  # mineral
        'a': 'کشاورزی',  # agriculture
        'e': 'ورازت نیرو',  # energy
    }
    proforma_invoice = models.CharField('شماره پیش فاکتور', max_length=50)
    beneficiary_country = models.ForeignKey(
        "dashboard.country", verbose_name='کشور ذینفع', on_delete=models.PROTECT)
    proforma_invoice_issue_date = models.DateField('تاریخ صدور پیش فاکتور')
    proforam_invoice_expire_date = models.DateField('تاریخ اعتبار پیش فاکتور')
    order_registration_case = models.ForeignKey(
        OrderRegistrationCase, verbose_name='حالت ثبت سفارش', on_delete=models.PROTECT)
    # supplier_type = models.CharField('نوع فروشنده‌ی حقیقی', choices=SUPPLIER_TYPE,max_length=1)
    supplier_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    related_object = GenericForeignKey('supplier_type', 'object_id')
    producer_type = models.CharField(
        'نوع واحدهای تولیدی', choices=PRODUCER_TYPE, max_length=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name='کاربر', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'اطلاعات اصلی'
        verbose_name_plural = 'اطلاعات اصلی'

    def __str__(self):
        return f'پرونده پیش فاکتور شماره'


class CuotmsAndShipping(models.Model):
    contract_type = models.ForeignKey(
        ContractType, verbose_name='نوع قرارداد', on_delete=models.PROTECT)
    shipping_all_at_once = models.BooleanField('حمل یکسره', default=False)
    shipping_period = models.BooleanField('حمل به دفعات', default=False)
    shipping_type = models.ManyToManyField(
        ShippingType, verbose_name='روش‌های حمل')

    class Meta:
        verbose_name = 'گمرکی و حمل'
        verbose_name_plural = 'گمرکی و حمل'

    def __str__(self):
        return self.name
