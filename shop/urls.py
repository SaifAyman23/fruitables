from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
    path('',views.shop,name='shop'),
    path('<str:cat_name>/',views.shop,name='shop'),
    path('product_details/<str:product_name>',views.product_details,name='product_details'),
    path('cart/',views.cart,name='cart'),
    path('search/',views.search,name='search'),
    path('remove_cart/<int:item_id>',views.remove_cart,name='remove_cart'),
    path('add_cart/<int:product_id>',views.add_cart,name='add_cart'),
    path('add_item/<int:item_id>',views.add_item,name='add_item'),
    path('remove_item/<int:item_id>',views.remove_item,name='remove_item'),
]
