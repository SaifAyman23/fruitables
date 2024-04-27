from django.db import models
from django.contrib.auth.models import User

def image_upload(instance,filename:str):
    extension=filename.split('.')[1]
    return f"products/{instance.name}.{extension}"

# Create your models here.
class Category(models.Model):
    title = models.CharField(verbose_name='Category Name' ,unique=True ,max_length=50)
    createdOn = models.DateField(verbose_name='Created On' ,auto_now=True)
    isAvailable = models.BooleanField(default=True,verbose_name=('Is Available'))
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self) -> str:
        return str(self.title).capitalize()
    
class Product(models.Model):
    name = models.CharField(verbose_name='Product Name',unique=True ,max_length=50)
    description = models.TextField(verbose_name='Description' ,max_length=200)
    price = models.IntegerField(verbose_name='Price')
    stock = models.IntegerField(verbose_name='Stock')
    addedOn = models.DateField(verbose_name='Addition Date' ,auto_now=True)
    images = models.ImageField(verbose_name='Image' ,upload_to=image_upload,null=True)
    category = models.ForeignKey(Category,verbose_name='Category' , on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.name).capitalize()
    

# class Review(models.Model):
#     user=

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

class Reviews(models.Model):
    user=models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    product=models.ForeignKey(Product, verbose_name=("Product"), on_delete=models.CASCADE)
    review=models.TextField(verbose_name=("Review"))
    date_created=models.DateField(verbose_name=("Creation date"), auto_now=True)

    class Meta:
        unique_together=(('user','product'),)
        verbose_name = ("Reviews")
        verbose_name_plural = ("Reviews")

    def __str__(self):
        return f"{self.user} / {self.product}"
    
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
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.f_name} {self.l_name}'

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
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