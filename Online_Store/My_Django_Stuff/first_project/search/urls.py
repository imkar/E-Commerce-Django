from django.urls import path

from .views import SearchProductView


urlpatterns = [
    #path('',views.productindex,name='productindex'),
    path('',SearchProductView.as_view(),name='searches'),
]
