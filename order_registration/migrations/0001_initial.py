# Generated by Django 5.1.5 on 2025-01-25 13:28

import django.db.models.deletion
import extensions.utils
import functools
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('dashboard', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=50, verbose_name='بانک')),
            ],
            options={
                'verbose_name': 'بانک',
                'verbose_name_plural': 'بانک',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'ارز',
                'verbose_name_plural': 'ارز',
            },
        ),
        migrations.CreateModel(
            name='CurrencySupply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'محل تامین ارز',
                'verbose_name_plural': 'محل تامین ارز',
            },
        ),
        migrations.CreateModel(
            name='Custom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'گمرک',
                'verbose_name_plural': 'گمرک',
            },
        ),
        migrations.CreateModel(
            name='ManufactureYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=10, verbose_name='سال تولید')),
            ],
            options={
                'verbose_name': 'سال تولید',
                'verbose_name_plural': 'سال تولید',
            },
        ),
        migrations.CreateModel(
            name='OrderRegistrationCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'حالت ثبت سفارش',
                'verbose_name_plural': 'حالت ثبت سفارش',
            },
        ),
        migrations.CreateModel(
            name='Packing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'نوع بسته بندی',
                'verbose_name_plural': 'نوع بسته بندی',
            },
        ),
        migrations.CreateModel(
            name='BankBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_registration.bank', verbose_name='شعبه بانک')),
            ],
            options={
                'verbose_name': 'شعبه بانک',
                'verbose_name_plural': 'شعبه بانک',
            },
        ),
        migrations.CreateModel(
            name='EntranceEdg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='نام')),
                ('customs', models.ManyToManyField(to='order_registration.custom', verbose_name='گمرک\u200cها')),
            ],
            options={
                'verbose_name': 'مرزهای ورودی',
                'verbose_name_plural': 'مرزهای ورودی',
            },
        ),
        migrations.CreateModel(
            name='MainData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.PositiveIntegerField(default=extensions.utils.generate_random_number, verbose_name='شماره پرونده')),
                ('proforma_invoice', models.CharField(max_length=50, verbose_name='شماره پیش فاکتور')),
                ('proforma_invoice_issue_date', models.DateField(verbose_name='تاریخ صدور پیش فاکتور')),
                ('proforam_invoice_expire_date', models.DateField(verbose_name='تاریخ اعتبار پیش فاکتور')),
                ('object_id', models.PositiveIntegerField()),
                ('producer_type', models.CharField(choices=[('i', 'صنعتی (بهین یاب)'), ('g', 'صنفی'), ('m', 'معدنی'), ('a', 'کشاورزی'), ('e', 'ورازت نیرو')], max_length=1, verbose_name='نوع واحدهای تولیدی')),
                ('status', models.CharField(choices=[('p', 'پیش نویس'), ('n', 'جدید'), ('r', 'ثبت سفارش')], default='p', max_length=1, verbose_name='وضعیت پرونده')),
                ('beneficiary_country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.country', verbose_name='کشور ذینفع')),
                ('supplier_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
                ('order_registration_case', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order_registration.orderregistrationcase', verbose_name='حالت ثبت سفارش')),
            ],
            options={
                'verbose_name': 'اطلاعات اصلی',
                'verbose_name_plural': 'اطلاعات اصلی',
            },
        ),
        migrations.CreateModel(
            name='Financial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proforma_amount', models.PositiveIntegerField(blank=True, default=None, verbose_name='مبلغ کل پیش فاکتور')),
                ('off_amount', models.PositiveIntegerField(blank=True, default=0, verbose_name='مبلغ تخفیف')),
                ('currency_operation_type', models.CharField(choices=[('b', 'بانکی'), ('nb', 'بدون انتقال ارز')], max_length=2, verbose_name='نوع عملیات ارزی')),
                ('shipping_price', models.PositiveIntegerField(blank=True, default=None, verbose_name='هزینه حمل')),
                ('other_price', models.PositiveIntegerField(blank=True, default=None, verbose_name='سایر هزینه\u200cهای')),
                ('payment_type', models.CharField(blank=True, choices=[('ca', 'نقدی'), ('cr', 'اعتباری')], default=None, max_length=2, verbose_name='نوع پرداخت')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order_registration.bank', verbose_name='بانک')),
                ('bank_branch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order_registration.bankbranch', verbose_name='شعبه بانکی')),
                ('curency_supply', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order_registration.currencysupply', verbose_name='تامین ارز')),
                ('currency_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order_registration.currency', verbose_name='نوع ارز')),
                ('main_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_registration.maindata', verbose_name='داده\u200cهای اصلی')),
            ],
            options={
                'verbose_name': 'مالی و بانکی',
                'verbose_name_plural': 'مالی و بانکی',
            },
        ),
        migrations.CreateModel(
            name='ShippingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('entrance_edge', models.ManyToManyField(to='order_registration.entranceedg', verbose_name='مرزهای ورودی')),
            ],
            options={
                'verbose_name': 'shippingtype',
                'verbose_name_plural': 'shippingtypes',
            },
        ),
        migrations.CreateModel(
            name='Incoterms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('code', models.CharField(max_length=50, verbose_name='کد')),
                ('shipping_type', models.ManyToManyField(to='order_registration.shippingtype', verbose_name='روش\u200cهای حمل و نقل')),
            ],
            options={
                'verbose_name': 'نوع قرارداد',
                'verbose_name_plural': 'نوع قرارداد',
            },
        ),
        migrations.CreateModel(
            name='CustomsAndShipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_all_at_once', models.BooleanField(default=False, verbose_name='حمل یکسره')),
                ('shipping_period', models.BooleanField(default=False, verbose_name='حمل به دفعات')),
                ('loading_location', models.CharField(blank=True, default=None, max_length=50, verbose_name='محل بارگیری')),
                ('shipping_nationality', models.CharField(choices=[('un', 'نامشخص'), ('ir', 'ایرانی'), ('fo', 'خارجی')], max_length=2, verbose_name='ناوگان حمل و نقل')),
                ('destination_custom', models.ManyToManyField(to='order_registration.custom', verbose_name='گمرک مقصد')),
                ('entrance_edge', models.ManyToManyField(to='order_registration.entranceedg', verbose_name='مرز ورودی')),
                ('incoterms', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order_registration.incoterms', verbose_name='نوع قرارداد')),
                ('main_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_registration.maindata', verbose_name='داده\u200cهای اصلی')),
                ('shipping_type', models.ManyToManyField(to='order_registration.shippingtype', verbose_name='روش\u200cهای حمل')),
            ],
            options={
                'verbose_name': 'گمرکی و حمل',
                'verbose_name_plural': 'گمرکی و حمل',
            },
        ),
        migrations.CreateModel(
            name='Ware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('virtual_code', models.PositiveIntegerField(default=functools.partial(extensions.utils.generate_random_number, *(10,), **{}), verbose_name='کد مجازی')),
                ('hs_code', models.PositiveSmallIntegerField(verbose_name='شماره تعرفه')),
                ('representation_status', models.CharField(choices=[('ma', 'واردات به سرزمین اصلی'), ('su', 'واردات به مناطق آزاد و ويژه اقتصادی')], max_length=2, verbose_name='وضعیت نمایندگی')),
                ('ware_identifier', models.PositiveSmallIntegerField(verbose_name='شناسه کالا')),
                ('organization_identifier', models.PositiveSmallIntegerField(verbose_name='شناسه سازمان')),
                ('persian_title', models.CharField(max_length=100, verbose_name='شرح تجاری فارسی')),
                ('english_title', models.CharField(max_length=100, verbose_name='شرح تجاری انگلیسی')),
                ('unit', models.CharField(choices=[('kg', 'کیلوگرم'), ('n', 'عدد'), ('m', 'متر'), ('mm', 'مترمربع'), ('mmm', 'مترمکعب'), ('l', 'لیتر'), ('p', 'جفت')], max_length=3, verbose_name='واحد اندازه گیری')),
                ('fob_price', models.PositiveSmallIntegerField(verbose_name='مبلغ FOB')),
                ('off', models.PositiveSmallIntegerField(verbose_name='تخفیف')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='تعداد/مقدار')),
                ('net_weight', models.PositiveSmallIntegerField(verbose_name='وزن خالص(کیلوگرم)')),
                ('gross_weight', models.PositiveSmallIntegerField(verbose_name='وزن ناخالص(کیلوگرم)')),
                ('status', models.CharField(max_length=1, verbose_name='وضعیت کالا')),
                ('technical_specifications', models.CharField(max_length=50, verbose_name='مشخصات فنی')),
                ('standard', models.CharField(max_length=50, verbose_name='استاندارد')),
                ('made_country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.country', verbose_name='کشور تولید کننده')),
                ('manufacture_year', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order_registration.manufactureyear', verbose_name='سال ساخت')),
                ('packing_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order_registration.packing', verbose_name='نوع بسته بندی')),
            ],
            options={
                'verbose_name': 'کالا',
                'verbose_name_plural': 'کالاها',
            },
        ),
    ]
