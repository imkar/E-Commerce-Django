# Generated by Django 3.0.3 on 2020-04-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0006_auto_20200326_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='distributer_info',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='model_number',
            field=models.IntegerField(null=True),
        ),
    ]
