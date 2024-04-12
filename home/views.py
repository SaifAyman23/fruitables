from django.shortcuts import render
from shop.models import *

# Create your views here.
def home(request):
    products_price=Product.objects.all().order_by('price')
    products_stock=Product.objects.all().order_by('stock')
    products=Product.objects.all()
    context={
        'products':products,
        'stocks':products_stock,
        'prices':products_price,
    }
    return render(request,'home/home.html',context)