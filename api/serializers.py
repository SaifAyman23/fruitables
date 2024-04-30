from rest_framework import serializers
from shop.models import *
from order.models import *
from cart.models import *
from rest_framework.authtoken.models import Token

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        
class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        fields='__all__'
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
        
class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderProduct
        fields='__all__'
        
class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model=Offer
        fields='__all__'
        
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model=Coupon
        fields='__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']
        extra_kwargs = {'password':{'write_only':True,'required':True}}