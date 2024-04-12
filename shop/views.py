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