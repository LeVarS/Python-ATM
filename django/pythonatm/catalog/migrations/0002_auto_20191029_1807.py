# Generated by Django 2.2.6 on 2019-10-29 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.IntegerField(help_text='Balance for Account'),
        ),
    ]
