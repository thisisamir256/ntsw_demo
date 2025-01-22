from django.db import models


class DocumentType(models.Model):
    name = models.CharField('نام', max_length=50)

    class Meta:
        verbose_name = 'نوع مدرک شناسایی'
        verbose_name_plural = 'نوع مدرک شناسایی'

    def __str__(self):
        return self.name


class supplier(models.Model):
    user = models.ForeignKey(
        "users.CustomUser",
        verbose_name='کاربر مربوطه',
        on_delete=models.CASCADE
    )
    status = models.BooleanField("وضعیت", default=True)
    description = models.TextField('توضیحات')
    identifier = models.PositiveIntegerField('شناسه فروشنده خارجی')
    created_at = models.DateField('تاریخ ایجاد', auto_now_add=False)
    # todo: add image upload

    class Meta:
        abstract = True


class Person(supplier):
    GENDER_CHOISES = {
        'mail': 'مرد',
        'fmail': 'زن'
    }
    MARIED_CHOISES = {
        's': 'مجرد',
        'm': 'متاهل',
        'c': 'متارکه',
        'w': 'بیوه',
    }

    first_name = models.CharField('نام/ First Name', max_length=100)
    last_name = models.CharField('نام خانوادگی/ Last Name', max_length=100)
    father_name = models.CharField('نام پدر', max_length=100)
    mother_name = models.CharField(
        'نام مادر',
        max_length=100,
        default=None,
        blank=True
    )
    grandfather_name = models.CharField(
        'نام جد',
        max_length=100,
        blank=True,
        default=None
    )
    country = models.ForeignKey(
        "dashboard.Country", verbose_name='کشور محل تولد', on_delete=models.PROTECT)
    city = models.CharField('شهر محل تولد', max_length=50,
                            default=None,  blank=True)
    gender = models.CharField('جنسیت', choices=GENDER_CHOISES, max_length=5)
    birthday = models.DateField('تاریخ تولد')
    nationality = models.ForeignKey(
        "dashboard.Country", verbose_name='ملیت', related_name='natinality_country', on_delete=models.PROTECT)
    maried = models.CharField(
        'وضعیت تاهل', max_length=50, choices=MARIED_CHOISES)  # tod: add choises
    personal_image = models.ImageField(
        'تصویر پرسنلی',
        upload_to='uploads/overseas_supplier/',
        max_length=1000,
        default=None,
        blank=True
    )
    document_type = models.ForeignKey(
        DocumentType,
        verbose_name='نوع مدرک شناسایی',
        on_delete=models.CASCADE
    )
    document_number = models.CharField('شماره مدرک شناسایی', max_length=100)
    issue_date = models.DateField('تاریخ صدور')
    expire_date = models.DateField('تاریخ انقضا')

    class Meta:
        verbose_name = 'شخص حقیقی'
        verbose_name_plural = 'شخص حقیقی'

    def __str__(self):
        return self.name


class Company(supplier):

    name = models.CharField('نام فارسی شرکت خارجی', max_length=100)
    en_name = models.CharField('نام لاتین شرکت خارجی', max_length=100)
    register_number = models.PositiveSmallIntegerField('شماره ثبت شرکت')
    company_type = models.CharField('نوع شرکت', max_length=50)
    registered_country = models.CharField('کشور محل ثبت', max_length=50)
    registered_date = models.DateField('تاریخ ثبت')
    registered_from = models.CharField('تابعیت ثبتی شرکت', max_length=50)
    owner_type = models.CharField('نوع مالکیت', max_length=50)
    country = models.CharField('کشور', max_length=50)
    city = models.CharField('شهر', max_length=50)
    address = models.TextField('آدرس')
    postal_code = models.PositiveSmallIntegerField('کد پستی')
    phone = models.CharField('شماره تلفن', max_length=20)
    status = models.BooleanField("وضعیت", default=True)
    description = models.TextField('توضیحات')
    identifier = models.PositiveIntegerField('شناسه فروشنده خارجی')

    class Meta:
        verbose_name = 'شرکت'
        verbose_name_plural = 'شرکت‌'

    def __str__(self):
        return self.name
