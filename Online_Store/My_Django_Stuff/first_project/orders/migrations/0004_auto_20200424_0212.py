# Generated by Django 3.0.3 on 2020-04-23 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_profile', '0002_auto_20200424_0212'),
        ('orders', '0003_auto_20200424_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery_profile.DeliveryProfile'),
        ),
    ]
