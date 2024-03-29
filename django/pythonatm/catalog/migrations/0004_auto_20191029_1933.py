# Generated by Django 2.2.6 on 2019-10-29 23:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20191029_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(help_text='Enter phone number for Account', max_length=10, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='atmachine',
            name='machine_id',
            field=models.CharField(help_text='Identification Number for ATM', max_length=16, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(16)]),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_number',
            field=models.CharField(help_text='Card number', max_length=16, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(16)]),
        ),
        migrations.AlterField(
            model_name='card',
            name='phone_number',
            field=models.CharField(help_text='Enter phone number for Account', max_length=10, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='card',
            name='pin',
            field=models.CharField(help_text='Enter PIN for Card', max_length=4, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(help_text='Identification Number for Transaction', max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
