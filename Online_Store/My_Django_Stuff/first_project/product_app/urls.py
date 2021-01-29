from django.urls import path

from .views import ProductListView,ProductDetailView,SkinCareListView,HairCareListView,TonicListView,CreamListView,FaceSetListView,justtesting,single_page,add_comment

urlpatterns = [
    #path('',views.productindex,name='productindex'),
    path('',ProductListView.as_view()),
    path('<slug:slug>/',ProductDetailSlugView.as_view(),name='slugview'),
    path('product_app/<int:id>/',views.ProductDetailView),
    path('skincare/',SkinCareListView.as_view(),name='skincare'),
    path('bodycare/',BodyCareListView.as_view(),name='bodycare'),
    path('haircare/',HairCareListView.as_view(),name='haircare'),
    path('tonic/',TonicListView.as_view(),name='tonic'),
    path('cream/',CreamListView.as_view(),name='cream'),
    path('faceset/',FaceSetListView.as_view(),name='faceset'),
    path('justtesting/',justtesting,name='justtesting'),
#    path('haircare/',haircare,name='haircare'),
    path('single_page/<slug:slug>/',single_page,name = 'single_page'),
    path('single_page/<slug:slug>/add_comment/',add_comment,name = 'add_comment'),
]
