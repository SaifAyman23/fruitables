from django.db import models
from shop.models import *

# Create your models here.
class OrderProduct(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    ordered = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Order Product")
        verbose_name_plural = ("Order Products")

    def __str__(self):
        return f"{self.order} / {self.product}"
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    first_name = models.CharField( max_length=250)
    last_name = models.CharField( max_length=250)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    address1 = models.TextField( max_length=250)
    address2 = models.TextField( max_length=250,blank=True,null=True)
    city = models.CharField( max_length=150)
    country = models.CharField( max_length=150,null=True)
    order_total = models.FloatField()
    grand_total = models.FloatField(null=True,blank=True)
    shipping = models.FloatField(default=50)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self,*args, **kwargs):
        self.grand_total=self.order_total+self.shipping
        super(Order,self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.first_name}'