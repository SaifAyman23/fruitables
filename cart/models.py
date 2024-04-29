from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product, verbose_name=("Product"), on_delete=models.CASCADE)
    quantity=models.IntegerField(verbose_name=("Quantity"))
    price=models.IntegerField(verbose_name=("Price"),null=True,blank=True,)
    total=models.IntegerField(verbose_name=("Total"),null=True,blank=True)
    
    class Meta:
        verbose_name = ("Cart")
        verbose_name_plural = ("Carts")
        
    def save(self,*args,**kwargs):
        if self.quantity > self.product.stock:
            self.quantity=self.product.stock
        if self.product.offer_price:
            self.price=self.product.offer_price
        else:
            self.price=self.product.price
        self.total=self.quantity*self.price
        super(Cart,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.product)

class Coupon(models.Model):
    coupon=models.CharField(verbose_name=("Coupon"),max_length=50)
    ratio=models.IntegerField(verbose_name=("Ratio"))
    created_at=models.DateField(verbose_name=("Created at"), auto_now=True)
    expiry_date=models.DateField(verbose_name=("Expires at"),null=True)
    is_available=models.BooleanField(verbose_name=("Is Available"),default=True)

    class Meta:
        verbose_name = ("Coupon")
        verbose_name_plural = ("Coupons")
        
    def save(self,*args,**kwargs):
        self.coupon=str(self.coupon).upper()
        super(Coupon,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.coupon).upper()