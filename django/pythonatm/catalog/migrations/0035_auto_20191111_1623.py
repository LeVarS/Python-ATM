# Generated by Django 2.2.6 on 2019-11-11 21:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0034_auto_20191111_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmachinerefill',
            name='refill_id',
            field=models.CharField(default='490799', help_text='Refill Identification Number for Transaction', max_length=6, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(default='6588938189', help_text='Identification Number for Transaction', max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
