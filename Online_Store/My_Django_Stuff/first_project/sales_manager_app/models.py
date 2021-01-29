from django.db import models
from product_app.models import Product
# Create your models here.
class SalesEmployee(models.Model):
    name = models.CharField(max_length=150)
    sid = models.IntegerField(primary_key=True)

    products_id = models.ForeignKey()
