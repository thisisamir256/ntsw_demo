# Generated by Django 5.1.5 on 2025-01-23 12:16

import django.db.models.deletion
import extensions.utils
import functools
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
        ('overseas_supplier', '0006_alter_company_created_at_alter_person_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyOwnerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'نوع مالکیت شرکت',
                'verbose_name_plural': 'نوع مالکیت شرکت',
            },
        ),
        migrations.CreateModel(
            name='CompanySubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='موضوع فعالیت')),
            ],
            options={
                'verbose_name': 'موضوع فعالیت شرکت',
                'verbose_name_plural': 'موضوع فعالیت شرکت',
            },
        ),
        migrations.CreateModel(
            name='CompanyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='نوع کمپانی')),
            ],
            options={
                'verbose_name': 'نوع شرکت',
                'verbose_name_plural': 'نوع شرکت',
            },
        ),
        migrations.AlterField(
            model_name='company',
            name='identifier',
            field=models.PositiveIntegerField(default=functools.partial(extensions.utils.generate_random_number, *(13,), **{}), verbose_name='شناسه فروشنده خارجی'),
        ),
        migrations.AlterField(
            model_name='company',
            name='postal_code',
            field=models.PositiveSmallIntegerField(blank=True, default=None, verbose_name='کد پستی'),
        ),
        migrations.AlterField(
            model_name='company',
            name='registered_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.country', verbose_name='کشور محل ثبت'),
        ),
        migrations.AlterField(
            model_name='company',
            name='registered_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='registered_from', to='dashboard.country', verbose_name='تابعیت ثبتی شرکت'),
        ),
        migrations.AlterField(
            model_name='person',
            name='personal_image',
            field=models.ImageField(blank=True, default=None, max_length=1000, upload_to='overseas_supplier/', verbose_name='تصویر پرسنلی'),
        ),
        migrations.AlterField(
            model_name='company',
            name='owner_type',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, to='overseas_supplier.companyownertype', verbose_name='نوع شرکت'),
        ),
        migrations.AddField(
            model_name='company',
            name='subject',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='overseas_supplier.companysubject', verbose_name='موضوع فعالیت شرکت'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='company_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='overseas_supplier.companytype', verbose_name='نوع شرکت'),
        ),
    ]
