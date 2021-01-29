from django.db import models
from product_app.models import Product
# Create your models here.
class ProductEmployee(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    product_id = models.ForeignKey('product_app.Product',on_delete=models.CASCADE)
