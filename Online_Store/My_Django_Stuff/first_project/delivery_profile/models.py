from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
# Create your models here.
User = settings.AUTH_USER_MODEL

class DeliveryProfile(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #customer_id

    def __str__(self):
        return self.email

# def delivery_profile_created_receiver(sender,instance,created,*args,**kwargs):
#     if created:
#         print("Send to stripe/braintree")
#         instance.customer_id = new_ID
#         instance.save()

def user_created_receiver(sender,instance,created,*args,**kwargs):
    if created and instance.email:
        DeliveryProfile.objects.get_or_create(user=instance,email=instance.email)

post_save.connect(user_created_receiver,sender=User)
