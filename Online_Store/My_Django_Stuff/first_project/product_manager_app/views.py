from django.shortcuts import render
from orders.models import Order
# Create your views here.
from django.http import HttpResponse


def pmanager_index(request):
    return HttpResponse("Hello, world. You're at the Product Manager index.")
