# Generated by Django 3.0.9 on 2020-08-22 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_manager', '0009_documentedinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentedinformation',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documentedinformation',
            name='title',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
    ]
