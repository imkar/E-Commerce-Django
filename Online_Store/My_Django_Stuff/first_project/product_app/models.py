import random
import os
from django.db import models
from django.db import models
from django.db.models.signals import pre_save,post_save

from first_project.utils import unique_slug_generator
'''
def product_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
'''
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance,filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,234225252)
    name , ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename=final_filename)


class ProductManager(models.Manager):
    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id) # Product.objects self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None



class Comment(models.Model):
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)




class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    slug = models.SlugField(blank=True)
    title = models.CharField(max_length=150,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=20,default=39.99)
    description = models.TextField()
    name = models.CharField(max_length=150)
    quantity_instocks = models.IntegerField()
    warranty_status = models.CharField(max_length=150)
    distributer_info = models.TextField(null=True)
    model_number = models.IntegerField(null=True)
    image_of_product = models.ImageField(upload_to=upload_image_path,null=True,blank=True)

    objects = ProductManager()

    def get_absolute_url(self):
        return "/products/{slug}/".format(slug=self.slug)
    def __str__(self):
        return str(self.name)
    def __unicode__(self):
        return self.name
'''
class ProdManager(models.Model):
    upload = models.ImageField(upload_to = user_directory_path)
    '''
def product_pre_save_receive(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receive,sender=Product)
