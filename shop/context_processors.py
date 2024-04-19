from .models import *

def cartItems(request,cartI=0):
    try:
        cartI=Cart.objects.all().count()
    except:
        pass
    return {'cartI':cartI}