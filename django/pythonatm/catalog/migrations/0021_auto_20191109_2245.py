# Generated by Django 2.2.6 on 2019-11-10 03:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_auto_20191109_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.CharField(default='637816699807', help_text='Enter Account Number', max_length=12, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(12)]),
        ),
    ]
