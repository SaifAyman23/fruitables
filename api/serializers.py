from rest_framework import serializers
from shop.models import *
from rest_framework.authtoken.models import Token

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        fields='__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']
        extra_kwargs = {'password':{'write_only':True,'required':True}}