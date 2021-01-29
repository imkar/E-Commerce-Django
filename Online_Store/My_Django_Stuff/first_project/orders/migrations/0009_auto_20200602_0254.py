# Generated by Django 3.0.3 on 2020-06-01 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('preparing', 'Preparing'), ('shipped', 'Shipped'), ('received', 'Received')], default='pending', max_length=120),
        ),
    ]