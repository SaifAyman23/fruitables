from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.decorators import api_view,action
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from .serializers import *

# Create your views here.
class ProductViewsets(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    
class CategoryViewsets(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
            
            
class ReviewViewsets(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]
    queryset=Reviews.objects.all()
    serializer_class=ReviewsSerializer
            
            
class OfferViewsets(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]
    queryset=Offer.objects.all()
    serializer_class=OfferSerializer
            
            
class CartViewsets(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
            
            
class CouponViewsets(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]
    queryset=Coupon.objects.all()
    serializer_class=CouponSerializer
            
            
class OrderViewsets(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
            
            
class OrderProductViewsets(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]
    queryset=OrderProduct.objects.all()
    serializer_class=OrderProductSerializer
    

class UserViewsets(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]
    queryset=User.objects.all()
    serializer_class=UserSerializer