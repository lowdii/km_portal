# Generated by Django 3.0.9 on 2020-08-20 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20200820_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='account.Unit'),
        ),
    ]