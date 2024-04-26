from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def shop(request,cat_name=None,catObj=None):
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
        'product':page_object,
        'number':page_number
    }
    return render(request,'shop/shop.html',context)

def search(request,keyword=None,category=None):
    if request.method == "POST":
        keyword=request.POST["keyword"]
        if keyword:
            print(keyword)
            cat=Category.objects.all()
            try:    
                try:
                    category=Category.objects.get(Q(title__icontains=keyword))
                    products=Product.objects.order_by('-addedOn').filter(Q(description__icontains=keyword) | Q(name__icontains=keyword) | Q(category=category))
                except:
                    print("HEREEEEEE")
                    products=Product.objects.order_by('-addedOn').filter(Q(description__icontains=keyword) | Q(name__icontains=keyword) )
                p = Paginator(products, 6)
                page_number=request.GET.get("page")
                page_object=p.get_page(page_number)
                print(page_number)
                context={
                    'category':cat,
                    'product':page_object,
                    'number':page_number,
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
    print('here')
    if request.method=='POST':
        rev=request.POST['review']
        try:
            print('update')
            revObj=Reviews.objects.get(user=request.user,product=product)
            revObj.review=rev
            revObj.save()
            print('done')
        except:
            print('create')
            review=Reviews(user=request.user,product=product,review=rev)
            review.save()
            print('done')
            
    context={
        'category':cat,
        'product':product,
        'products':products,
        'reviews':reviews
    }
    return render(request,'shop/product_details.html',context)



def cart(request,subTotal=0,shipping=50,grandTotal=0,discount=0,originalTotal=0):
    try:
        try:
            cartItem=Cart.objects.all().filter(user=request.user)
            print('HIIII')
            for item in cartItem:
                subTotal+=item.total
        except:
            cartItem=None
        if request.method=='POST':
            print('HIIII2')
            
            discount=request.POST['coupon']
            if discount:
                try:
                    coupon=Coupon.objects.get(coupon=str(discount))
                    grandTotal=subTotal+shipping
                    originalTotal=grandTotal
                    discount=grandTotal*(coupon.ratio/100)
                    grandTotal=int(grandTotal-discount)
                except:
                    pass
        else:
            shipping=50
            grandTotal=subTotal+shipping
    except:
        pass
    context={
        'subTotal':subTotal,
        'grandTotal':grandTotal,
        'shipping':shipping,
        'discount':discount,
        'originalTotal':originalTotal,
        'cartItem':cartItem,
    }
    
    return render(request,'shop/cart.html',context)

def remove_cart(request,item_id):
    
    cartItem=Cart.objects.get(id=item_id)
    cartItem.delete()
    
    return redirect('shop:cart')

def add_item(request,item_id):
    cartItem=Cart.objects.get(id=item_id)
    cartItem.quantity+=1
    cartItem.save()
    
    return redirect('shop:cart')

def remove_item(request,item_id):
    cartItem=Cart.objects.get(id=item_id)
    if cartItem.quantity>1:
        cartItem.quantity-=1
        cartItem.save()
    else:
        cartItem.delete()
    return redirect('shop:cart')

def add_cart(request,product_id,cartItem=None):
    product=Product.objects.get(id=product_id)
    print(str('asdasdasdasd'))
    
    try:
        cartItem=Cart.objects.get(user=request.user,product=product)
        print(cartItem)
    except:pass
    if cartItem:
        cartItem.quantity+=1
        cartItem.save()
        print(cartItem," EXISTS")
    else:
        print("SAVED")
        if request.method=='POST':
            print("SAVED2")
            amount=int(request.POST["quantity"])
            print(amount)
            if amount:
                cartItem=Cart(user=request.user,product=product,quantity=amount)
                cartItem.save()
        else:
            print('HEREEEEEEE')
            return redirect("shop:product_details")
    return redirect("shop:cart")