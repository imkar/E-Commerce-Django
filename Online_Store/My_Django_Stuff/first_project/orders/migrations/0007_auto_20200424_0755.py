# Generated by Django 3.0.3 on 2020-04-24 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_delivery_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='delivery_address',
            new_name='shipadr',
        ),
    ]