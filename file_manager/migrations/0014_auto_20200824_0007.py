# Generated by Django 3.0.9 on 2020-08-24 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_manager', '0013_remove_documenttype_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentedinformation',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documenttype',
            name='description',
            field=models.TextField(default='test description'),
            preserve_default=False,
        ),
    ]
