from django.shortcuts import render,redirect
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



def cart(request,subTotal=0,shipping=50,grandTotal=5,discount=None,originalTotal=None):
    try:
        cartItem=Cart.objects.all()
        print('HIIII')
        for item in cartItem:
            subTotal+=item.total
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
    try:
        cartItem=Cart.object.get(id=item_id)
        cartItem.delete()
    except:
        pass
    
    return redirect('shop:cart')