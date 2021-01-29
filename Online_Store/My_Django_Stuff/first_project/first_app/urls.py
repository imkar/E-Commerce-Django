from django.urls import path
from first_app import views


# TEMPLATE URLS !
app_name = 'first_app'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('',views.index,name='index'),
    path('login/',views.user_login,name='user_login')
]
