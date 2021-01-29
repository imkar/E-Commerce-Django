# Generated by Django 3.0.3 on 2020-03-21 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_app', '0002_product_image_of_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductEmployee',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.Product')),
            ],
        ),
    ]