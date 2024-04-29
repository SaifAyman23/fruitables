from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='accounts:login_view')
def cart(request,subTotal=0,shipping=50,grandTotal=0,discount=0,originalTotal=0):
    try:
        try:
            cartItem=Cart.objects.all().filter(user=request.user)
            for item in cartItem:
                subTotal+=item.total
        except:
            cartItem=None
        if request.method=='POST':
            
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
    
    return render(request,'cart/cart.html',context)

def remove_cart(request,item_id):
    
    cartItem=Cart.objects.get(id=item_id)
    cartItem.delete()
    
    return redirect('cart:cart')

def add_item(request,item_id):
    cartItem=Cart.objects.get(id=item_id)
    cartItem.quantity+=1
    cartItem.save()
    
    return redirect('cart:cart')

def remove_item(request,item_id):
    cartItem=Cart.objects.get(id=item_id)
    if cartItem.quantity>1:
        cartItem.quantity-=1
        cartItem.save()
    else:
        cartItem.delete()
    return redirect('cart:cart')

@login_required(login_url='accounts:login_view')
def add_cart(request,product_id,cartItem=None):
    product=Product.objects.get(id=product_id)
    
    try:
        cartItem=Cart.objects.get(user=request.user,product=product)
    except:pass
    if cartItem:
        cartItem.quantity+=1
        cartItem.save()
    else:
        if request.method=='POST':
            amount=int(request.POST["quantity"])
            if amount:
                cartItem=Cart(user=request.user,product=product,quantity=amount)
                cartItem.save()
        else:
            return redirect("cart:product_details")
    return redirect("cart:cart")