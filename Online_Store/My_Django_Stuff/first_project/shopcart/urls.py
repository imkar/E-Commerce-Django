from django.urls import path

from .views import shopping_cart,add_to_cart,remove_from_cart,checkout,firststep,creditcard,laststep


urlpatterns = [
    #path('',shopping_cart,name='shopcart'),
    path('remove_from_cart/<int:id>',remove_from_cart,name='remove_from_cart'),
    path('add_to_cart/<slug:slug>',add_to_cart,name='add_to_cart'),
    path('checkout/',checkout,name='checkout'),
    path('firststep/',firststep,name ='firststep'),
    path('stepadr/',stepadr,name ='stepadr'),
    path('laststep/',laststep,name ='laststep'),
    path('creditcard/',creditcard,name ='creditcard'),

    #path('delitem/<id>/',delitem,name='delitem'),
]
