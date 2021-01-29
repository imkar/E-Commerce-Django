from django.urls import path

from . import views


urlpatterns = [
    path('',views.pmanager_index,name='pmanager_index'),

]
