# Generated by Django 3.0.9 on 2020-08-24 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_manager', '0012_auto_20200824_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documenttype',
            name='description',
        ),
    ]