"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from django.urls import include
from first_app.views import user_login,index,user_logout
from product_app.views import ProductDetailView,product_detail_view,ProductListView,ProductDetailSlugView,BodyCareListView,SkinCareListView,TonicListView,CreamListView,FaceSetListView,HairCareListView,justtesting,single_page,add_comment
from shopcart.views import firststep,add_to_cart,remove_from_cart,stepadr,creditcard,laststep
from accountinfo.views import account_info,prev_orders,addresses_list,del_adr,update_name,update_surname,invoice_order,add_adr
urlpatterns = [
    path('',index,name='index'),
    #path('product_app/',include('product_app.urls')),
    path('product_app/<int:id>',ProductDetailView.as_view()),
    #path('products/<slug:slug>/',ProductDetailSlugView.as_view(),name='slugview'),
    #path('product_manager_app/',include('product_manager_app.urls')),
    #path('register/',register,name='register'),
    path('products/',ProductListView.as_view(),name='products'),
    #path('products/<int:pk>',ProductDetailView.as_view()),
    path('login/',user_login,name='user_login'),
    path('admin/', admin.site.urls),
    path('logout/',user_logout,name='logout'),
    path('search/',include("search.urls"),name='search'),
    #path('special/',views.special,name='special'),
    path('products/skincare/',SkinCareListView.as_view(),name='skincare'),
    path('products/bodycare/',BodyCareListView.as_view(),name='bodycare'),
    path('products/tonic/',TonicListView.as_view(),name='tonic'),
    path('products/cream/',CreamListView.as_view(),name='cream'),
    path('products/faceset/',FaceSetListView.as_view(),name='faceset'),
    path('products/haircare/',HairCareListView.as_view(),name='haircare'),
        path('justtesting/',justtesting,name='justtesting'),
    path('products/single_page/<slug:slug>/',single_page,name = 'single_page'),
    #path('shopping_cart/',include("shopcart.urls"),name='shopcart'),
    path('firststep/',firststep,name ='firststep'),
    path('stepadr/',stepadr,name ='stepadr'),
    path('creditcard/',creditcard,name ='creditcard'),
    path('laststep/',laststep,name ='laststep'),
    path('add_to_cart/<slug:slug>',add_to_cart,name='add_to_cart'),
    path('remove_from_cart/<int:id>',remove_from_cart,name='remove_from_cart'),
    path('single_page/<slug:slug>/add_comment/',add_comment,name = 'add_comment'),
    path('account_info/',account_info,name='account_info'),
    path('prev_orders/',prev_orders,name='prev_orders'),
    path('addresses_list/',addresses_list,name='addresses_list'),
    path('del_adr/<adr_name>/',del_adr,name='del_adr'),
    path('update_name/',update_name,name='update_name'),
    path('update_surname/',update_surname,name='update_surname'),
    path('invoice_order/<order_id>/',invoice_order,name='invoice_order'),
    path('add_adr/',add_adr,name='add_adr'),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
