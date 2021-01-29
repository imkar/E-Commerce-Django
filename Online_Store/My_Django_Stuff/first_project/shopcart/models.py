from django.conf import settings
from django.db import models
from product_app.models import Product
from django.db.models.signals import pre_save,post_save,m2m_changed
User = settings.AUTH_USER_MODEL

class CartItem(models.Model):
    cart = models.ForeignKey('Cart',null=True,blank = True,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(default = 10.99,max_digits=1000,decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add = True,auto_now = False)
    updated = models.DateTimeField(auto_now_add=False,auto_now = True)

    def __unicode__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.title


class Cart(models.Model):
    total = models.DecimalField(max_digits=100,decimal_places= 2, default = 0.00)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "Cart id: %s" %(self.id)

# class CartManager(models.Manager):
#     def new_or_get(self,reques,id):
#         cart_id = request.session.get("cart_id", None)
#         qs = self.get_queryset().filter(id = cart_id)
#         if qs.count() == 1 :
#             new_obj = False
#             cart_obj = qs.first()
#             if request.user.is_authenticated and cart_obj.user is None:
#                 cart_obj.user = request.user
#                 cart_obj.save()
#         else:
#             cart_obj = Cart.objects.new(user=request.user)
#             new_obj = True
#             request.session['cart_id'] = cart_obj.id
#         return cart_obj ,new_obj
#
#     def new(self,user=None):
#         user_obj = None
#         if user is not None:
#             if user.is_authenticated:
#                 user_obj = user
#         return self.model.objects.create(user=user_obj)
#     def get(self,request,id):
#         cart_id = request.session.get("cart_id", None)
#         qs = self.get_queryset().filter(id = cart_id)
#         cart_obj = qs.first()
#         if request.user.is_authenticated and cart_obj.user is None:
#             cart_obj.user = request.user
#             cart_obj.save()
#
# class Cart(models.Model):
#     user= models.ForeignKey(User,null=True, blank =True,on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product,blank = True)
#     total = models.DecimalField(default=0.00,max_digits=100,decimal_places = 2)
#     updated = models.DateTimeField(auto_now=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     objects = CartManager()
#
#     def __str__(self):
#         return str(self.id)
#
# def pre_save_cart_receiver(sender,instance,action,*args,**kwargs):
#     print(action)
#     if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
#         products = instance.products.all()
#         total = 0
#         for item in products:
#             total += item.price
#         print(total)
#         instance.total = total
#         instance.save()
#
# m2m_changed.connect(pre_save_cart_receiver,sender=Cart.products.through)
