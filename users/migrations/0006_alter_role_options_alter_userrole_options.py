# Generated by Django 5.1.5 on 2025-01-19 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_role_userrole'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name': 'نقش', 'verbose_name_plural': 'نقش\u200cها'},
        ),
        migrations.AlterModelOptions(
            name='userrole',
            options={'verbose_name': 'نقش کاربر', 'verbose_name_plural': 'نقش کاربران'},
        ),
    ]
