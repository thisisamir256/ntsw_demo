from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from django.core.exceptions import ValidationError
from extensions.utils import generate_random_number
from functools import partial

rand_with_10_digits = partial(generate_random_number, 10)


class OrderRegistrationCase(models.Model):
    title = models.CharField('عنوان', max_length=50)

    class Meta:
        verbose_name = 'حالت ثبت سفارش'
        verbose_name_plural = 'حالت ثبت سفارش'

    def __str__(self):
        return self.title


class Custom(models.Model):
    title = models.CharField('عنوان', max_length=50)

    class Meta:
        verbose_name = 'گمرک'
        verbose_name_plural = 'گمرک'

    def __str__(self):
        return self.title


class EntranceEdg(models.Model):
    title = models.CharField('نام', max_length=50)
    customs = models.ManyToManyField(Custom, verbose_name='گمرک‌ها')

    class Meta:
        verbose_name = 'مرزهای ورودی'
        verbose_name_plural = 'مرزهای ورودی'

    def __str__(self):
        return self.title


class ShippingType(models.Model):
    title = models.CharField('عنوان', max_length=50)
    entrance_edge = models.ManyToManyField(
        EntranceEdg, verbose_name='مرزهای ورودی')

    class Meta:
        verbose_name = "shippingtype"
        verbose_name_plural = "shippingtypes"

    def __str__(self):
        return self.title


class Incoterms(models.Model):
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
    identifier = models.PositiveIntegerField(
        'شماره پرونده', default=generate_random_number)
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


class Currency(models.Model):
    title = models.CharField('عنوان', max_length=50)

    class Meta:
        verbose_name = 'ارز'
        verbose_name_plural = 'ارز'

    def __str__(self):
        return self.title


class CustomsAndShipping(models.Model):
    SHIPPING_NATIONALITY = {
        'un': 'نامشخص',  # uncertain
        'ir': 'ایرانی',  # iranian
        'fo': 'خارجی',  # foreign
    }
    main_data = models.ForeignKey(
        MainData, verbose_name='داده‌های اصلی', on_delete=models.CASCADE)
    incoterms = models.ForeignKey(
        Incoterms, verbose_name='نوع قرارداد', on_delete=models.PROTECT)
    shipping_all_at_once = models.BooleanField('حمل یکسره', default=False)
    shipping_period = models.BooleanField('حمل به دفعات', default=False)
    shipping_type = models.ManyToManyField(
        ShippingType, verbose_name='روش‌های حمل')
    entrance_edge = models.ManyToManyField(
        EntranceEdg, verbose_name='مرز ورودی')
    destination_custom = models.ManyToManyField(
        Custom, verbose_name='گمرک مقصد')
    loading_location = models.CharField(
        'محل بارگیری', max_length=50, default=None, blank=True)
    shipping_nationality = models.CharField(
        'ناوگان حمل و نقل', choices=SHIPPING_NATIONALITY, max_length=2)

    class Meta:
        verbose_name = 'گمرکی و حمل'
        verbose_name_plural = 'گمرکی و حمل'

    def __str__(self):
        return self.name


class Bank(models.Model):
    title = models.CharField('بانک', max_length=50, default=None, blank=True)

    class Meta:
        verbose_name = 'بانک'
        verbose_name_plural = 'بانک'

    def __str__(self):
        return self.title


class BankBranch(models.Model):
    title = models.CharField('عنوان', max_length=50)
    bank = models.ForeignKey(
        Bank, verbose_name='شعبه بانک', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'شعبه بانک'
        verbose_name_plural = 'شعبه بانک'

    def __str__(self):
        return self.name


class CurrencySupply(models.Model):
    title = models.CharField('عنوان', max_length=50)

    class Meta:
        verbose_name = 'محل تامین ارز'
        verbose_name_plural = 'محل تامین ارز'

    def __str__(self):
        return self.title


class Financial(models.Model):
    CURRENCY_OPERATION_TYPE_CHOISES = {
        'b': 'بانکی',
        'nb': 'بدون انتقال ارز',
    }
    PAYMENT_TYPE_CHOISES = {
        'ca': 'نقدی',
        'cr': 'اعتباری',
    }
    main_data = models.ForeignKey(
        MainData, verbose_name='داده‌های اصلی', on_delete=models.CASCADE)
    proforma_amount = models.PositiveIntegerField(
        'مبلغ کل پیش فاکتور', default=None, blank=True)
    currency_type = models.ForeignKey(
        Currency, verbose_name='نوع ارز', on_delete=models.PROTECT)
    off_amount = models.PositiveIntegerField(
        'مبلغ تخفیف', default=0, blank=True)
    currency_operation_type = models.CharField(
        'نوع عملیات ارزی', choices=CURRENCY_OPERATION_TYPE_CHOISES, max_length=2)
    bank = models.ForeignKey(Bank, verbose_name='بانک',
                             on_delete=models.PROTECT)
    bank_branch = models.ForeignKey(
        BankBranch, verbose_name='شعبه بانکی', on_delete=models.PROTECT)
    curency_supply = models.ForeignKey(
        CurrencySupply, verbose_name='تامین ارز', on_delete=models.PROTECT)
    shipping_price = models.PositiveIntegerField(
        'هزینه حمل', default=None, blank=True)
    other_price = models.PositiveIntegerField(
        'سایر هزینه‌های', default=None, blank=True)
    payment_type = models.CharField(
        'نوع پرداخت', choices=PAYMENT_TYPE_CHOISES, max_length=2, default=None, blank=True)

    class Meta:
        verbose_name = 'مالی و بانکی'
        verbose_name_plural = 'مالی و بانکی'

    def __str__(self):
        return self.name


class ManufactureYear(models.Model):
    year = models.CharField('سال تولید', max_length=10)

    class Meta:
        verbose_name = 'سال تولید'
        verbose_name_plural = 'سال تولید'

    def __str__(self):
        return self.year


class Packing(models.Model):
    title = models.CharField('عنوان', max_length=10)

    class Meta:
        verbose_name = 'نوع بسته بندی'
        verbose_name_plural = 'نوع بسته بندی'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("PackingType_detail", kwargs={"pk": self.pk})


class Ware(models.Model):
    # کالاهای پرونده
    REPRESENTATION_STATUS_CHOICES = {
        'ma': 'واردات به سرزمین اصلی',  # main area
        'su': 'واردات به مناطق آزاد و ويژه اقتصادی'  # sub area
    }
    UNIT_CHOISES = {
        'kg': 'کیلوگرم',
        'n': 'عدد',
        'm': 'متر',
        'mm': 'مترمربع',
        'mmm': 'مترمکعب',
        'l': 'لیتر',
        'p': 'جفت',

    }
    STAUS_CHOICES = {
        'n': 'نو',
        'u': 'مستعمل',
        'r': 'بازسازی شده',
        'w': 'پسماند',
    }
    virtual_code = models.PositiveIntegerField(
        'کد مجازی', default=rand_with_10_digits)
    hs_code = models.PositiveSmallIntegerField('شماره تعرفه')
    representation_status = models.CharField(
        'وضعیت نمایندگی', choices=REPRESENTATION_STATUS_CHOICES, max_length=2)
    # identifier may be link to product_identifier model
    ware_identifier = models.PositiveSmallIntegerField('شناسه کالا')
    organization_identifier = models.PositiveSmallIntegerField('شناسه سازمان')
    persian_title = models.CharField('شرح تجاری فارسی', max_length=100)
    english_title = models.CharField('شرح تجاری انگلیسی', max_length=100)
    manufacture_year = models.ForeignKey(
        ManufactureYear, verbose_name='سال ساخت', on_delete=models.PROTECT)
    unit = models.CharField(
        'واحد اندازه گیری', max_length=3, choices=UNIT_CHOISES)
    fob_price = models.PositiveSmallIntegerField('مبلغ FOB')
    off = models.PositiveSmallIntegerField('تخفیف')
    amount = models.PositiveSmallIntegerField('تعداد/مقدار')
    net_weight = models.PositiveSmallIntegerField('وزن خالص(کیلوگرم)')
    gross_weight = models.PositiveSmallIntegerField('وزن ناخالص(کیلوگرم)')
    packing_type = models.ForeignKey(
        Packing,
        verbose_name='نوع بسته بندی',
        on_delete=models.PROTECT
    )
    status = models.CharField('وضعیت کالا', max_length=1)
    made_country = models.ForeignKey(
        "dashboard.country", verbose_name='کشور تولید کننده', on_delete=models.PROTECT)
    technical_specifications = models.CharField('مشخصات فنی', max_length=50)
    standard = models.CharField('استاندارد', max_length=50)

    class Meta:
        verbose_name = 'کالا'
        verbose_name_plural = 'کالاها'
        constraints = [
            models.CheckConstraint(
                check=models.Q(technical_specifications_isnull=False) | models.Q(
                    standard_isnull=False),
                name='technical_specifications_or_standard_not_null'
            )
        ]

    def __str__(self):
        return self.name

    def clean(self):
        super.clean()
        if not self.technical_specifications and not self.standard:
            return ValidationError(f'{self.technical_specifications} , {self.standard} نمی‌تواند همزمان خالی باشد.')


# class Documents(models.Model):
#     main_data = models.ForeignKey(
#         MainData, verbose_name='مستندات', on_delete=models.PROTECT)

#     class Meta:
#         verbose_name = 'مستدات پرونده'
#         verbose_name_plural = 'مستندات پرونده'

#     def __str__(self):
#         return self.
