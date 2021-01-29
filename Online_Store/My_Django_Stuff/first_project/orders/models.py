import math
from django.db import models
from django.db.models.signals import pre_save,post_save
from shopcart.models import Cart
from first_project.utils import unique_order_id_generator
from delivery_profile.models import DeliveryProfile
from address_app.models import Address
from datetime import date
# Create your models here.
ORDER_STATUS_CHOICES = (
    ('pending','Pending'),
    ('preparing','Preparing'),
    ('shipped','Shipped'),
    ('received','Received'),

)


class Order(models.Model):
    delivery_profile = models.ForeignKey(DeliveryProfile,null = True,blank=True,on_delete=models.CASCADE)
    order_id = models.CharField(max_length=120,blank=True) #delivery_id
    cart = models.ForeignKey(Cart,null=True,blank=True,on_delete=models.CASCADE)
    status = models.CharField(max_length=120,default='pending',choices=ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(default = 5.99,max_digits = 100, decimal_places = 2 )
    total = models.DecimalField(default = 5.99,max_digits = 100, decimal_places = 2 )
    active = models.BooleanField(default=True)
    shipadr= models.ForeignKey(Address,null=True,blank=True,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=date.today)
    ### IN OUR ER DIAGRAM
    # customer_id
    # Quantity
    # is_delivered
    # total_price
    # delivery_adress
    # product_ud
    def __str__(self):
        return self.order_id
    def update_total(self):
        cart_total = self.cart.total
        shipping_total = self.shipping_total
        new_total = math.fsum([cart_total,shipping_total])
        format_t = format(new_total,'.2f')
        self.total = format_t
        self.save()
        return new_total

def pre_save_create_order_id(sender,instance,*args,**kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)

pre_save.connect(pre_save_create_order_id,sender=Order)

def post_save_cart_total(sender,instance,created,*args,**kwargs):
    if not created:
        if instance is not None:
            cart_obj = instance
            cart_total = cart_obj.total
            cart_id = cart_obj.id
            qs = Order.objects.filter(cart__id = cart_id)
            if qs.count() == 1:
                order_obj = qs.first()
                order_obj.update_total()

post_save.connect(post_save_cart_total,sender=Cart)

def post_save_order(sender,instance,created,*args,**kwargs):
    # print("running")
    if created:
        # print("Updating first . . .")
        instance.update_total()

post_save.connect(post_save_order,sender=Order)
