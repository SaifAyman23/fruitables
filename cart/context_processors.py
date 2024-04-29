from .models import *

def cartItems(request,cartI=0):
    try:
        cartI=Cart.objects.filter(user=request.user).count()
    except:
        cartI=0
    return {'cartI':cartI}