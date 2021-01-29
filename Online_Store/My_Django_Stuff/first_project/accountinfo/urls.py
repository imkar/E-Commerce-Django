from django.urls import path

from .views import account_info,prev_orders,addresses_list,del_adr,update_name,update_surname,invoice_order,add_adr

urlpatterns = [
    path('account_info/',account_info,name='account_info'),
    path('prev_orders/',prev_orders,name='prev_orders'),
    path('addresses_list/',addresses_list,name='addresses_list'),
    path('del_adr/<adr_name>/',del_adr,name='del_adr'),
    path('update_name/',update_name,name='update_name'),
    path('update_surname/',update_surname,name='update_surname'),
    path('invoice_order/<order_id>/',invoice_order,name='invoice_order'),
    path('add_adr/',add_adr,name='add_adr'),
]
