from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def orders(request,orders=None,order_products=None):
    try:
        orders=Order.objects.all().filter(user=request.user)
        order_products=OrderProduct.objects.all().filter(user=request.user)
    except:
        pass
    context={
        'orders':orders,
        'order_products':order_products,
    }
    return render(request,'order/orders.html',context)

def checkout(request,subTotal=0,shipping=0):
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
            address2 = address2 if address2 else 'None'
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
                )
                order.order_total+=subTotal
                order.save()
            except:
                order=Order(
                    user=request.user,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    address1=address1,
                    address2=address2,
                    city=city,
                    country=country,
                    order_total=subTotal,
                    shipping=shipping
                )
                order.save()
                
            for item in cartItems:
                try:
                    orderProduct=OrderProduct.objects.get(user=request.user,order=order,product=item.product)
                    orderProduct.quantity+=item.quantity
                    orderProduct.product_price+=item.total
                    orderProduct.save()
                    item.delete()
                except:
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
            'subTotal':subTotal,
            'shipping':shipping
        }
        return render(request,'order/chackout_page.html',context)
    return render("shop:cart")

def cancel_order(request,order_id):
    Order.objects.get(id=order_id).delete()
    return redirect('order:orders')