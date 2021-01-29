from django.db import models
from delivery_profile.models import DeliveryProfile

# Create your models here.
ADDRESS_TYPES = (
    ('billing','Billing'),
    ('shipping','Shipping'),
)

class Address(models.Model):
    address_name = models.CharField(null=True,blank=True,max_length=120)
    delivery_profile = models.ForeignKey(DeliveryProfile,null=True,blank=True,on_delete=models.CASCADE)
    # address_type = models.CharField(max_length=120,choices = ADDRESS_TYPES)
    address_1 = models.CharField(max_length=120,null=True,blank=True)
    # address_2 = models.CharField(max_length=120,null=True,blank=True)
    # city = models.CharField(null=True,blank=True,max_length=120)
    # country = models.CharField(max_length=120,default = 'Turkey')
    # state = models.CharField(max_length=120)
    # postal_code = models.CharField(max_length=120)

    def __str__(self):
        return str(self.delivery_profile)
