from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render,get_object_or_404,Http404
# Create your views here.
from django.http import HttpResponse
from .models import Product
from comments.forms import CommentForm
from comments.models import Comment
from django.http import HttpResponseRedirect
from shopcart.models import Cart


def justtesting(request):
    template = "product/Prod.html"
    return render(request,template,{})



class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/product_category.html'

    def get_context_data(self,*args,**kwargs):
        context = super(ProductListView,self).get_context_data(*args,**kwargs)
        print(context)
        return context


# def product_list_view(request):
#     context = {
#         'object_list': queryset
#     }
#     return render(request,"product/product_list_view.html",context)

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/product_category.html'

    def get_context_data(self,*args,**kwargs):
        context = super(ProductDetailSlugView,self).get_context_data(*args,**kwargs)
        request = self.request
        cart_obj,new_obj = Cart.objects.new_or_get(request)
        context['cart'] = cart_obj
        return context
    def get_object(self,*args,**kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product,slug=slug,active=True)
        try:
            instance = Product.objects.get(slug=slug) #, active can be added
        except Product.DoesNotExist:
            raise Http404("Product Not Found . . .")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "product/details.html"

    def get_context_data(self,*args,**kwargs):
        context = super(ProductDetailView,self).get_context_data(*args,**kwargs)
        print(context)
        # context['abc'] = 123
        return context

def product_detail_view(request,*args,**kwargs):
    print(args)
    print(kwargs)
    instance = Product.objects.get(pk=pk) #id of the product
    context = {
        'object': instance
    }
    return render(request,"product/details.html",context)


class SkinCareListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/product_category.html'

    def get_queryset(self,*args,**kwargs):
        request = self.request
        title = self.kwargs.get('name')
        return Product.objects.filter(title__icontains='Cilt Bakımı')
        #context = super(SkinCareListView,self).get_queryset(*args,**kwargs)
        #print(context)
def single_page(request,slug):
    instance = Product.objects.get(slug=slug)
    comments = Comment.objects.filter(product=instance)
    context = {
        'obj' : instance,
        'comments' : comments
    }
    return render(request,"product/single_page.html",context)

def add_comment(request,slug):
    url = request.META.get('HTTP_REFERER') # get last url
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.product = Product.objects.get(slug=slug)
            current_user = request.user
            data.user = current_user
            data.save()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)


class BodyCareListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/product_category.html'

    def get_queryset(self,*args,**kwargs):
        request = self.request
        title = self.kwargs.get('title')
        return Product.objects.filter(title__icontains='Vucut Bakımı')
        #context = super(SkinCareListView,self).get_queryset(*args,**kwargs)
        #print(context)

class HairCareListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/product_category.html'

    def get_queryset(self,*args,**kwargs):
        request = self.request
        title = self.kwargs.get('name')
        return Product.objects.filter(name__icontains='hair')
        #context = super(SkinCareListView,self).get_queryset(*args,**kwargs)
        #print(context)

class TonicListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/product_category.html'
    def get_queryset(self,*args,**kwargs):
        request = self.request
        title = self.kwargs.get('name')
        return Product.objects.filter(name__icontains='Tonic')
        #context = super(SkinCareListView,self).get_queryset(*args,**kwargs)
        #print(context)

class CreamListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/product_category.html'
    def get_queryset(self,*args,**kwargs):
        request = self.request
        title = self.kwargs.get('name')
        return Product.objects.filter(name__icontains='Cream')
        #context = super(SkinCareListView,self).get_queryset(*args,**kwargs)
        #print(context)

class FaceSetListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/product_category.html'
    def get_queryset(self,*args,**kwargs):
        request = self.request
        title = self.kwargs.get('name')
        return Product.objects.filter(name__icontains='face')
        #context = super(SkinCareListView,self).get_queryset(*args,**kwargs)
        #print(context)
# def skincare(request):
#     try:
#         obj = Product.objects.filter(name__icontains='Cilt') #, active can be added
#     except Product.DoesNotExist:
#         raise Http404("Product Not Found . . .")
#     content = {
#         'obj':obj
#     }
#     return render(request,"product/product_category.html",content)
