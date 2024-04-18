from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
    path('',views.shop,name='shop'),
    path('product_details/<str:product_name>',views.product_details,name='product_details'),
    path('cart/',views.cart,name='cart'),
    path('remove_cart/<int:id>',views.remove_cart,name='remove_cart'),
]
