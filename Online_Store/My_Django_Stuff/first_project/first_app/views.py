from django.contrib.auth import authenticate,login,logout,get_user_model
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse,HttpResponseRedirect,HttpResponse
from .forms import RegisterForm,LoginForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from product_app.models import Product

# Create your views here.

def index(request):
    #my_dict = {'insert_me':"Now I am from views.py !"}
    if request.method == 'GET':
        print(request.user.groups.first())
        return render(request,'index/index.html', {'products': Product.objects.all()})

    if request.method == 'POST':
        if "name" in request.POST:
            image = request.FILES.get('uploaded_image')
            name = request.POST['name']
            price = request.POST['price']
            stock = request.POST['stock']
            info = request.POST['info']
            Product.objects.create(name=name, price=price, quantity_instocks=stock,
                                description=info, image_of_product=image)
            messages.success(request, 'Product added successfully')
            return render(request,'index/index.html', {'products': Product.objects.all()})
        else:
            key = request.POST['id']
            stock = request.POST['stock']
            product = Product.objects.get(id=key)
            product.quantity_instocks = stock
            product.save()
            return render(request,'index/index.html', {'products': Product.objects.all()})


@login_required
def special(request):
    return HttpResponse("You are logged in, Have Fun!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


User = get_user_model()
def user_login(request):
    regform = RegisterForm(request.POST or None)
    logform = LoginForm(request.POST or None)

    context = {
        "regform" : regform,
        "logform": logform
    }
    ## REGISTRATION FORM here
    if regform.is_valid():
        print(regform.cleaned_data)
        username = regform.cleaned_data.get("username")
        email = regform.cleaned_data.get("email")
        password = regform.cleaned_data.get("password")
        print(request.user.is_authenticated)
        new_user = User.objects.create_user(username,email,password)
        print(request.user.is_authenticated)
        print(new_user)
    #return render(request,"first_app/loginsignup.html",context)


    print("User logged in")
    print(request.user.is_authenticated)
    if logform.is_valid():
        print(logform.cleaned_data)
        username = logform.cleaned_data.get("username")
        password = logform.cleaned_data.get("password")
        user = authenticate(request,username=username,password=password)
        print(user)
        print(request.user.is_authenticated)
        if user is not None:
            print(request.user.is_authenticated)
            login(request,user)
            #context['form'] = LoginForm()
            return HttpResponseRedirect(reverse('index'))
        else:

            print("Error")

    return render(request,"login/loginsignup.html",context)
