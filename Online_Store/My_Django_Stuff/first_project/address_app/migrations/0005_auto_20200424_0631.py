# Generated by Django 3.0.3 on 2020-04-24 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_app', '0004_auto_20200424_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
