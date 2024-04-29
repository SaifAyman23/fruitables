from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
import reportlab
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Create your views here.
def shop(request):
    cat=Category.objects.all()
    product=Product.objects.all().filter(stock__gt=0).order_by('-offer')
    products=Product.objects.all().order_by('-offer')
    p = Paginator(product, 6)
    page_number=request.GET.get("page")
    page_object=p.get_page(page_number)
    context={
        'category':cat,
        'products':products,
        'product':page_object,
        'number':page_number,
    }
    return render(request,'shop/shop.html',context)

def shop_price(request):
    if request.method=="POST":
        prices=request.POST['amount']
        cat=Category.objects.all()
        product=Product.objects.all().filter(price__lte=prices)
        products=Product.objects.all().order_by('-offer')
        p = Paginator(product, 6)
        page_number=request.GET.get("page")
        page_object=p.get_page(page_number)
        context={
            'category':cat,
            'products':products,
            'product':product,
            'number':page_number,
        }
        return render(request,'shop/shop.html',context)
    
    return redirect('shop:shop')

def shop_cats(request,cat_name=None,catObj=None,product=None):
    products=Product.objects.all().order_by('-offer')
    try:
        catObj=Category.objects.get(title=cat_name)
        cat=Category.objects.all()
        product=Product.objects.all().filter(category=catObj)
    except:
        cat=Category.objects.all()
        product=Product.objects.all()
    p = Paginator(product, 6)
    page_number=request.GET.get("page")
    page_object=p.get_page(page_number)
    context={
        'cat_obj':catObj,
        'category':cat,
        'products':products,
        'product':page_object,
        'number':page_number
    }
    return render(request,'shop/shop.html',context)

def search(request,keyword=None,category=None):
    product=Product.objects.all().order_by('-offer')
    if request.method == "POST":
        keyword=request.POST["keyword"]
        if keyword:
            cat=Category.objects.all()
            try:    
                try:
                    category=Category.objects.get(Q(title__icontains=keyword))
                    products=Product.objects.order_by('-addedOn').filter(Q(description__icontains=keyword) | Q(name__icontains=keyword) | Q(category=category))
                except:
                    products=Product.objects.order_by('-addedOn').filter(Q(description__icontains=keyword) | Q(name__icontains=keyword) )
                p = Paginator(products, 6)
                page_number=request.GET.get("page")
                page_object=p.get_page(page_number)
                context={
                    'category':cat,
                    'product':page_object,
                    'number':page_number,
                    'products':product,
                }
                return render(request,'shop/shop.html',context)
            except:pass
        
    return redirect("shop:shop")
        
    

def product_details(request,product_name,reviews=None):
    product=Product.objects.get(name=product_name)
    products=Product.objects.all()
    
    cat=Category.objects.all()
    try:
        reviews=Reviews.objects.all().filter(product=product)
    except:pass
    if request.method=='POST':
        rev=request.POST['review']
        try:
            revObj=Reviews.objects.get(user=request.user,product=product)
            revObj.review=rev
            revObj.save()
        except:
            review=Reviews(user=request.user,product=product,review=rev)
            review.save()
            
    context={
        'category':cat,
        'product':product,
        'products':products,
        'reviews':reviews
    }
    return render(request,'shop/product_details.html',context)




