# Generated by Django 5.1.5 on 2025-01-20 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_qualifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesscard',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان ارسال'),
        ),
    ]
