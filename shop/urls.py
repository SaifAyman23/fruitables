from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
    path('',views.shop,name='shop'),
    path('product_details/<str:product_name>',views.product_details,name='product_details'),
]
