from django.db import models
from product_app.models import Product
from django.contrib.auth.models import User
    # Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete =models.CASCADE,blank=True,default=True)
    product = models.ForeignKey(Product,on_delete =models.CASCADE,blank=True,default=True)
    rate = models.IntegerField(default=1)
    subject = models.CharField(max_length=50,blank=True)
    comment = models.CharField(max_length=250,blank=True)
    name = models.CharField(max_length=80)
    email= models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment "{}" by {}'.format(self.comment,self.user)
