from django.shortcuts import render
from orders.models import Order
from delivery_profile.models import DeliveryProfile
from address_app.models import Address
from django.http import HttpResponseRedirect
# Create your views here.
def account_info(request):
    template = "AccountInfo/Account.html"
    return render(request,template,{})


def prev_orders(request):
    template = "previousorders/Previous-Orders.html"
    user = request.user
    deli_prof = DeliveryProfile.objects.get(user=user)
    user_order = Order.objects.filter(delivery_profile=deli_prof)
    context = {
        'order' : user_order,


    }
    return render(request,template,context)


def addresses_list(request):
    template = "addresses/Addresses.html"
    user = request.user
    print(user)
    deli_prof = DeliveryProfile.objects.get(user=user)
    adress = Address.objects.filter(delivery_profile=deli_prof)
    context = {
        'adrname' : adress
    }
    return render(request,template,context)

def del_adr(request,adr_name):
    url = request.META.get('HTTP_REFERER')
    instance = Address.objects.filter(address_name=adr_name)
    instance.delete()
    return HttpResponseRedirect(url)



def add_adr(request):
    url = request.META.get('HTTP_REFERER')
    user = request.user
    instance = request.GET['adress_new']
    # Adr_info = Address.objects.filter(address_name=instance)
    # if Adr_info:

    print(instance)
    user_mail =user.email
    del_prof = DeliveryProfile.objects.get(email=user_mail)

    instance2 = request.GET['adress_part']
    print(instance2)
    new_addr = Address.objects.create(address_name=instance,delivery_profile=del_prof,address_1=instance2)
    new_addr.save()

    return HttpResponseRedirect(url)
# def edit_adr(request,adr_name):
#     url = request.META.get('HTTP_REFERER')
#     instance = Address.objects.filter(address_name=adr_name)
#     instance.delete()
#     return HttpResponseRedirect(url)

def update_name(request):
    url = request.META.get('HTTP_REFERER')
    instance = request.POST['name_inp']
    print(instance)
    user = request.user
    user.first_name =instance
    user.save()
    return HttpResponseRedirect(url)

def update_surname(request):
    url = request.META.get('HTTP_REFERER')
    instance = request.POST['last_name_inp']
    print(instance)
    user = request.user
    user.last_name =instance
    user.save()
    return HttpResponseRedirect(url)

def invoice_order(request,order_id):
    template = "invoice/invoice.html"
    order = Order.objects.get(order_id=order_id)
    print(order)
    delivery_prof = order.delivery_profile
    print(delivery_prof)
    cartingen = order.cart
    print(cartingen)

    context = {
        'order_obj' : order,
        'delivery_profile' : delivery_prof,
        'cart' : cartingen
    }
    return render(request,template,context)
