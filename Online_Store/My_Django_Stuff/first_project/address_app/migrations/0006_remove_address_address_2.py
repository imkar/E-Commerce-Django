# Generated by Django 3.0.3 on 2020-04-24 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address_app', '0005_auto_20200424_0631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='address_2',
        ),
    ]
