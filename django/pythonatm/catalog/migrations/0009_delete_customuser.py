# Generated by Django 2.2.6 on 2019-11-02 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20191101_2148'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]