from django.shortcuts import render
from .models import *

# Create your views here.
def shop(request):
    cat=Category.objects.all()
    product=Product.objects.all()
    context={
        'category':cat,
        'product':product,
    }
    return render(request,'shop/shop.html',context)

def product_details(request,product_name):
    product=Product.objects.get(name=product_name)
    products=Product.objects.all()
    cat=Category.objects.all()
    context={
        'category':cat,
        'product':product,
        'products':products,
    }
    return render(request,'shop/product_details.html',context)