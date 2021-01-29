# Generated by Django 3.0.3 on 2020-04-24 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_profile', '0002_auto_20200424_0212'),
        ('address_app', '0003_auto_20200424_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='address_2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='delivery_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery_profile.DeliveryProfile'),
        ),
    ]