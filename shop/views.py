from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def shop(request):
    
    cat=Category.objects.all()
    product=Product.objects.all()
    p = Paginator(product, 6)
    page_number=request.GET.get("page")
    page_object=p.get_page(page_number)
    context={
        'category':cat,
        'product':page_object,
        'number':page_number
    }
    return render(request,'shop/shop.html',context)

def shop_cats(request,cat_name=None,catObj=None):
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
                    products=Product.objects.order_by('-addedOn').filter(Q(description__icontains=keyword) | Q(name__icontains=keyword) )
                p = Paginator(products, 6)
                page_number=request.GET.get("page")
                page_object=p.get_page(page_number)
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

@login_required(login_url='accounts:login_view')
def add_cart(request,product_id,cartItem=None):
    product=Product.objects.get(id=product_id)
    
    try:
        cartItem=Cart.objects.get(user=request.user,product=product)
        print(cartItem)
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
            return redirect("shop:product_details")
    return redirect("shop:cart")

def checkout(request,grandTotal=0):
    try:
        cartItems=Cart.objects.all().filter(user=request.user)
    except:pass
    if cartItems:
        
        if request.method=="POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone = request.POST['phone']
            address1 = request.POST['address1']
            address2 = request.POST['address2']
            city = request.POST['city']
            country = request.POST['country']
            try:
                order=Order.objects.get(
                    user=request.user,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    address1=address1,
                    address2=address2,
                    city=city,
                    country=country,
                    order_total=grandTotal
                )
            except:
                order=Order(
                    user=request.user,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    address1=address1,
                    address2=address2 if address2 else 'None',
                    city=city,
                    country=country,
                    order_total=grandTotal
                )
                
            order.save()
            for item in cartItems:
                orderProduct=OrderProduct()
                orderProduct.user=request.user
                orderProduct.order=order
                orderProduct.product=item.product
                orderProduct.product_price=item.total
                orderProduct.quantity=item.quantity
                orderProduct.save()
                item.delete()
            
            return redirect('home:home')
        context={
            'cartItems':cartItems,
            'grandTotal':grandTotal,
        }
        return render(request,'shop/chackout_page.html',context)
    return render("shop:cart")