from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
    path('',views.shop,name='shop'),
    path('price',views.shop_price,name='shop_price'),
    path('cats/<str:cat_name>/',views.shop_cats,name='shop_cats'),
    path('product_details/<str:product_name>',views.product_details,name='product_details'),
    path('search',views.search,name='search'),
]
