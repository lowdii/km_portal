# Generated by Django 3.0.9 on 2020-08-20 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_manager', '0007_documenttype_secratariatlevel_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.IntegerField(choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=2020, unique=True),
        ),
    ]
