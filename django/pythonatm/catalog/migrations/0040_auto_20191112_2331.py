# Generated by Django 2.2.6 on 2019-11-13 04:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0039_transaction_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='first_name',
            field=models.CharField(help_text='Enter first name of Card Holder', max_length=30),
        ),
        migrations.AlterField(
            model_name='card',
            name='last_name',
            field=models.CharField(help_text='Enter last name of Card Holder', max_length=30),
        ),
        migrations.AlterField(
            model_name='card',
            name='phone_number',
            field=models.CharField(help_text='Enter phone number for Card Holder', max_length=10, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
