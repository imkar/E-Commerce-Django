from django.shortcuts import render
from product_app.models import Product
from django.http import HttpResponse,HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .models import Cart,CartItem
from delivery_profile.models import DeliveryProfile
from address_app.forms import AddressForm
from orders.models import Order
from address_app.models import Address
from django.contrib import messages
import os
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
import datetime
from xhtml2pdf import pisa
# from django.core.mail import send_mail
from django.core.mail import EmailMessage
import glob
def generate_PDF(request,context):
    data = context

    template = get_template('invoice/invoice.html')
    html  = template.render(context = data)

    file = open( str(data['order_obj']) +'.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
            encoding='utf-8')

    file.seek(0)
    pdf = file.read()
    file.close()
    return HttpResponse(pdf, 'application/pdf')




#from address_app.forms import AddressForm
# Create your views here.
# def shopping_cart(request):
#     cart_obj,new_obj = Cart.objects.new_or_get(request)
#     return render(request ,'cart/newcart.html',{"cart":cart_obj})

# def shopping_cart(request):
#     try:
#
#     except:
#         the_id = None
#     if the_id:
#         cart = Cart.objects.get(id=the_id)
#         context = {"cart":cart}
#     else:
#         empty_message = "Your Cart is Empty, please keep shopping."
#         context = {"empty":True,"empty_message":empty_message}
#
#     template = "cart/shoppingcart.html"
#     return render(request,template,context)
def firststep(request):
    template = "cart_steps/firststep.html"
    template2 = "cart_steps/address.html"
    cart = None
    # cart_id = request.session['cart_id']
    try:
        cart_id = request.session['cart_id']
    except:
        cart = Cart()
        cart.save()
        request.session['cart_id'] = cart.id
        cart_id = cart.id

    cart_id = request.session.get('cart_id')

    if cart_id is None:
        cart = Cart.objects.create()
        cart_id = cart.id
        request.session['cart_id'] = cart.id
    order_obj = None
    if cart_id:
        cart = Cart.objects.get(id=cart_id)

    # order_obj = Order.objects.create(cart = cart)

    user = request.user
    delivery_profile = None

    if user.is_authenticated:
        delivery_profile,delivery_profile_created = DeliveryProfile.objects.get_or_create(user = user,email=user.email,active=True)
    if delivery_profile is not None:
        order_qs = Order.objects.filter(delivery_profile=delivery_profile,cart=cart)
        if order_qs.count() == 1:
            order_obj= order_qs.first()
        else:
            old_order_qs = Order.objects.exclude(delivery_profile=delivery_profile).filter(cart=cart,active=True)
            if old_order_qs.exists():
                old_order_qs.update(active=False)
            order_obj = Order.objects.create(delivery_profile=delivery_profile,cart=cart)
            # context = {"cart":cart,"order_obj":order_obj,"delivery_profile":delivery_profile}
            # return HttpResponseRedirect(reverse(stepadr))
    if 'first_next' in request.POST:
        context = {"cart":cart,"order_obj":order_obj,"delivery_profile":delivery_profile}
        return HttpResponseRedirect(reverse(stepadr))
    context = {"cart":cart,"order_obj":order_obj,"delivery_profile":delivery_profile}
    return render(request,template,context)


def stepadr(request):
    template = "cart_steps/address.html"
    template2 = "cart_steps/creditcard.html"
    # try:
    #     the_id = request.session[id]
    #     print("id of cart in second Stepper : ",the_id)
    # except:
    #     the_id = None
    #     print("id of cart in firststep : ",the_id)
    cart = None
    cart_id = request.session['cart_id']
    try:
        cart=Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except :
        cart = Cart()
        cart.save()
        cart_id = cart_id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)

    if cart_id:
        print("Items of cart getting . . . ")
        cart = Cart.objects.get(id=cart_id)
        print("Cart Object :",cart)
        user = request.user
        if user.is_authenticated:
            print("YEEEAAA its authenticated babe!")
            delivery_profile,delivery_profile_created = DeliveryProfile.objects.get_or_create(user = user,email=user.email,active=True)
            print("Is that delivery profile created for real ? ",delivery_profile)
        if delivery_profile is not None:
            order_qs = Order.objects.filter(delivery_profile=delivery_profile,cart=cart)
            print("Give me that QS : ",order_qs)
            if order_qs.count() == 1:
                order_obj= order_qs.first()
                print("We got only one my friend : ", order_obj)
            else:
                old_order_qs = Order.objects.exclude(delivery_profile=delivery_profile).filter(cart=cart,active=True)
                if old_order_qs.exists():
                    old_order_qs.update(active=False)
        if 'submission' in request.POST:
            print("It is submission time!")

            adres = None
            adresname_new = request.POST.get('companyName')
            adresnum_new = request.POST.get('companyAddress')
            adresname = request.POST['cars']
            if adresname_new and adresnum_new  :
                adres = Address(address_name=adresname_new,address_1=adresnum_new,delivery_profile=delivery_profile)
            elif adresname != 'None':
                print("address name : " , adresname)
                get_adr = Address.objects.get(address_name=adresname)
                print("get_adr : ",get_adr)
                adresnum = get_adr.address_1
                print("address : " , adresnum)
                adres = Address.objects.get(address_name=adresname,address_1=adresnum,delivery_profile=delivery_profile)
            else:
                url = request.META.get('HTTP_REFERER')
                return HttpResponseRedirect(url)
            #print(adres)
            adres.save()
            # order_obj = Order.objects.create(delivery_profile=delivery_profile,cart=cart,delivery_adress=adres)
            # addres_id = request.session.get("addres_id")
            print("addres_id")
            print(order_obj)
            older = order_obj
            order_obj,created  = Order.objects.get_or_create(delivery_profile=delivery_profile,cart=cart,shipadr=adres)
            order_obj.save()
            print(order_obj)
            older.delete()
            context = {"cart":cart,"order_obj":order_obj,"delivery_profile":delivery_profile}
            return HttpResponseRedirect(reverse(creditcard))

    Adr = Address.objects.filter(delivery_profile=delivery_profile)
    context = {"cart":cart,"order_obj":order_obj,"delivery_profile":delivery_profile,"adr":Adr}
    return render(request,template,context)

def creditcard(request):
    template = "cart_steps/creditcard.html"

    if 'golast' in request.POST:
        return HttpResponseRedirect(reverse(laststep))
    # context = {"cart":cart,"order_obj":order_obj,"delivery_profile":delivery_profile}
    return render(request,template,{})




def laststep(request):
    template = "cart_steps/laststep.html"
    cart = None
    cart_id = request.session['cart_id']
    try:
        cart=Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except :
        cart = Cart()
        cart.save()
        cart_id = cart_id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    if cart_id:
        print("Items of cart getting . . . ")
        cart = Cart.objects.get(id=cart_id)
        print("Cart Object :",cart)
        user = request.user
        if user.is_authenticated:
            print("YEEEAAA its authenticated babe!")
            delivery_profile,delivery_profile_created = DeliveryProfile.objects.get_or_create(user = user,email=user.email,active=True)
            print("Is that delivery profile created for real ? ",delivery_profile)
        if delivery_profile is not None:
            order_qs = Order.objects.filter(delivery_profile=delivery_profile,cart=cart)
            print("Give me that QS : ",order_qs)
            if order_qs.count() == 1:
                order_obj= order_qs.first()
                print("We got only one my friend : ", order_obj)
            else:
                old_order_qs = Order.objects.exclude(delivery_profile=delivery_profile).filter(cart=cart,active=True)
                if old_order_qs.exists():
                    old_order_qs.update(active=False)

    context = {"cart":cart,"order_obj":order_obj,"delivery_profile":delivery_profile}
    generate_PDF(request.POST,context)
    del request.session['cart_id']
    try :
        print("im here bro ???")
        email = EmailMessage('Hello','Test invoice mail (Fake invoice just for testing)','testforwebsite1232@gmail.com', [context['delivery_profile']])
        print(os.listdir('*.pdf'))
        print("im here bro ???")
        email.attach(glob.glob('g3ok4rd9qm.pdf'))
        email.send()
        print("im here bro ???")
        print("sended")
    except:
        pass
    return render(request,template,context)




# def shopping_cart(request):
#     # somecase = False
#     # gotodiv = False
#
#     template = "cart/shoppingcart.html"
#     template2 = "invoice/invoice.html"
#     cart = None
#     try:
#         the_id = request.session['cart_id']
#     except:
#         the_id = None
#
#
#     order_obj = None
#     if the_id:
#         cart = Cart.objects.get(id=the_id)
#         #order_obj = Order.objects.create(cart = cart)
#     user = request.user
#
#     delivery_profile = None
#     if user.is_authenticated:
#         delivery_profile,delivery_profile_created = DeliveryProfile.objects.get_or_create(user = user,email=user.email,active=True)
#     if delivery_profile is not None:
#         order_qs = Order.objects.filter(delivery_profile=delivery_profile,cart=cart)
#         if order_qs.count() == 1:
#             order_obj= order_qs.first()
#         else:
#             old_order_qs = Order.objects.exclude(delivery_profile=delivery_profile).filter(cart=cart,active=True)
#             if old_order_qs.exists():
#                 old_order_qs.update(active=False)
#             order_obj = Order.objects.create(delivery_profile=delivery_profile,cart=cart)
#
#     # address_form = AddressForm(request.POST or None)
#     print("Created address_form")
#     # if address_form.address.name:
#     #     print(address_form.address_1)
#     # if address_form.is_valid():
#     #     print("HERE AS WELL")
#     #     print(request.POST)
#     #
#     #     instance = address_form.save(commit=False)
#     #     addresname = request.POST.get('companyName')
#     #     addres_1 = request.POST.get('companyAddress')
#     #     print("also saved everything ")
#     #     order_obj.delivery_adress = instance.address_name
#     #     return HttpResponseRedirect("/")
#
#     if 'submission' in request.POST:
#
#         print("iamhere too")
#
#         print("iamhere too")
#         adresname = request.POST.get('companyName')
#         print("iamhere too")
#         adresnum = request.POST.get('companyAddress')
#         print("iamhere too")
#         adres = Address(address_name=adresname,address_1=adresnum,delivery_profile=delivery_profile)
#         #print(adres)
#
#         adres.save()
#         # order_obj = Order.objects.create(delivery_profile=delivery_profile,cart=cart,delivery_adress=adres)
#         # addres_id = request.session.get("addres_id")
#         print("addres_id")
#         print(order_obj)
#         older = order_obj
#         order_obj,created  = Order.objects.get_or_create(delivery_profile=delivery_profile,cart=cart,shipadr=adres)
#         order_obj.save()
#         print(order_obj)
#         older.delete()
#         context = {"cart":cart,"order_obj":order_obj,"delivery_profile":delivery_profile}
#         return render(request,template2,context)
#         #instance.save()
#         # somecase = True
#         # if somecase:
#         #     gotodiv = 'step11'
#         #     print("Sorry Murat :(")
#         #     return render(request,'cart/shoppingcart.hmtl' step11,context)
#             #gotodiv = 'step11'
#             #context = {"cart":cart,"order_obj":order_obj,"delivery_profile":delivery_profile}
#     # else:
#     #     empty_message = "Your Cart is Empty, please keep shopping."
#     #     context = {"empty":True,"empty_message":empty_message}
#     #     return render(request,template,context)
#
#
#     context = {"cart":cart,"order_obj":order_obj,"delivery_profile":delivery_profile}
#
#     print("atshoopingcart2\n")
#     # if not somecase:
#     return render(request,template,context)


def add_to_cart(request,slug):
    request.session.set_expiry(120000)
    try:
        the_id = request.session['cart_id']
        print(the_id)
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id = the_id)
    print(cart)
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass

    if request.method == "POST":
        print(request.method)
        qty = request.POST['qty']
        print(qty)
        if product.quantity_instocks > int(qty):
            print("Instocks : ",product.quantity_instocks)
            product.quantity_instocks -= int(qty)
            product.save()
            print("Instocks now: ",product.quantity_instocks)
            if int(qty) <= 0 :
                messages.error(request,"In order to add this item to the cart, quantity must be bigger than 0")
            else:
                #if product in cart:

                cart_item = CartItem.objects.create(cart = cart,product=product)
                print(cart_item)
                cart_item.quantity = qty
                cart_item.save()
                print("item saved")
                new_total = 0.00
                for item in cart.cartitem_set.all():
                    print(item)
                    line_total = float(item.product.price) * item.quantity
                    print(item.product.price)
                    new_total += line_total
                    item.line_total = line_total
                    print(item)
                    print(item.line_total)
                    item.save()
                request.session['items_total'] = cart.cartitem_set.count()
                cart.total = new_total
                cart.save()
        else:
            messages.error(request,"Dont have enough products in stocks!!")
    return HttpResponseRedirect(reverse("firststep"))

def remove_from_cart(request,id):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse("firststep"))

    cartitem = CartItem.objects.get(id=id)
    print("cart item in stocks :",cartitem.product.quantity_instocks)
    cartitem.product.quantity_instocks = cartitem.product.quantity_instocks + cartitem.quantity
    cartitem.product.save()
    print("Quantity",cartitem.quantity)
    cartitem.delete()
    new_total = 0.00
    for item in cart.cartitem_set.all():
        print(item)
        line_total = float(item.product.price) * item.quantity
        print(item.product.price)
        new_total += line_total
        item.line_total = line_total
        print(item)
        print(item.line_total)
        item.save()
    request.session['items_total'] = cart.cartitem_set.count()
    cart.total = new_total
    cart.save()

    return HttpResponseRedirect(reverse("firststep"))


def checkout(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None

    if the_id == None :
        return HttpResponseRedirect(reverse("shopcart"))
    else:
        cart = Cart.objects.get(id=the_id)
        if cart.cartitem_set.count() == 0:
            return HttpResponseRedirect(reverse("shopcart"))
        else:
            order_obj, new_order_obj = Order.objects.get_or_create(cart = cart)

    user = request.user
    delivery_profile = None
    if user.is_authenticated:
        delivery_profile = None
    context = {"order_obj":order_obj,"delivery_profile":delivery_profile}
    return render(request,"cart/checkout.html",context)

#
# def update(request):
#     product_id = request.POST.get('product_id')
#     #remove_id = request.POST.get('remove_id')
#     print(product_id)
#     #print(remove_id)
#     if product_id is not None :
#         try:
#             product_object = Product.objects.get(id=product_id)
#             print(product_object)
#         except Product.DoesNotExist:
#             print("This product does not exist!")
#             return HttpResponseRedirect(reverse("shopcart"))
#         # TODO: Quantity check !
#         # try:
#         #     product_obj = Product.objects.get(quantity=product_id)
#         # except Product.DoesNotExist:
#         #     print("This product does not exist!")
#         #     return HttpResponseRedirect(reverse("shopcart"))
#         cart_obj, new_obj = Cart.objects.new_or_get(request,id)
#         if product_object in cart_obj.products.all():
#             print("HEREEEEE")
#             cart_obj.products.remove(product_object)
#             print("DELETED")
#         else:
#             print("I am added bro")
#             cart_obj.products.add(product_object)
#     return HttpResponseRedirect(reverse("shopcart"))

#
# def delitem(request,id):
#     # try:
#     #     the_id = request.session['cart_id']
#     #     cart = Cart.objects.get(id = the_id)
#     # except:
#     #     return HttpResponseRedirect(reverse("shopcart"))
#     cart_obj = Cart.objects.new_or_get(request,id)
#     product_object = Product.objects.get(id=id)
#     cart_obj.products.delete(product_object)
#     # product_id = request.POST.get('hope')
#     # print("why not HEREEEEE")
#     # print(product_id)
#     # if product_id is not None:
#     #     product_object = Product.objects.get(id=product_id)
#     #     cart_obj, new_obj = Cart.objects.new_or_get(request)
#     #     print(cart_obj)
#     #     if product_object in cart_obj.products.all():
#     #         cart_obj.products.remove(product_object)
#     return HttpResponseRedirect(reverse("shopcart"))
