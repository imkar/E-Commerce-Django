from django.db.models import Q
from django.shortcuts import render
from django.views.generic.list import ListView
from product_app.models import Product
# Create your views here.
class SearchProductView(ListView):
    template_name = 'search/product_category.html'

    def get_queryset(self,*args,**kwargs):
        request = self.request
        # print(request.GET)
        query = request.GET.get('q')
        # print(query)
        if query is not None:
            lookups = Q(name__icontains=query) | Q(title__icontains=query) | Q(id__icontains=query) | Q(price__contains=query) | Q(description__icontains=query) | Q(quantity_instocks__icontains=query) | Q(warranty_status__icontains=query) | Q(distributer_info__icontains=query) | Q(model_number__icontains=query)
            return Product.objects.filter(lookups).distinct()
        return Product.objects.none()
        '''
        __icontains = field constains this
        __iexact = fields is exactly this
        '''
