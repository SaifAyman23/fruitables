from django.urls import path
from . import views

app_name='order'

urlpatterns = [
    path('',views.orders,name='orders'),
    path('checkout/<int:subTotal>/<int:shipping>',views.checkout,name='checkout'),
    path('cancel/<int:order_id>',views.cancel_order,name='cancel'),
    path('approve/<int:order_id>',views.approve_order,name='approve'),
]
