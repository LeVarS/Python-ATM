# Generated by Django 2.2.6 on 2019-11-13 04:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0040_auto_20191112_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(help_text='Enter first name of account holder', max_length=30, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(help_text='Enter last name of account holder', max_length=30, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(help_text='Enter phone number of account holder', max_length=10, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='atmachine',
            name='machine_id',
            field=models.CharField(help_text='Identification Number for ATM', max_length=16, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(16)], verbose_name='ATM'),
        ),
        migrations.AlterField(
            model_name='card',
            name='first_name',
            field=models.CharField(help_text='Enter first name of card holder', max_length=30),
        ),
        migrations.AlterField(
            model_name='card',
            name='last_name',
            field=models.CharField(help_text='Enter last name of card holder', max_length=30),
        ),
        migrations.AlterField(
            model_name='card',
            name='phone_number',
            field=models.CharField(help_text='Enter phone number for card holder', max_length=10, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
