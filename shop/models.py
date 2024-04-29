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
    
class Offer(models.Model):
    title=models.CharField(verbose_name=("Title"),max_length=50)
    ratio=models.IntegerField(verbose_name=("Ratio"))
    created_at=models.DateField(verbose_name=("Created at"), auto_now=True)
    expiry_date=models.DateField(verbose_name=("Expires at"),null=True)
    is_available=models.BooleanField(verbose_name=("Is Available"),default=True)
    
    def __str__(self):
        return str(self.title)

class Product(models.Model):
    name = models.CharField(verbose_name='Product Name',unique=True ,max_length=50)
    description = models.TextField(verbose_name='Description' ,max_length=200)
    price = models.IntegerField(verbose_name='Price')
    stock = models.IntegerField(verbose_name='Stock')
    addedOn = models.DateField(verbose_name='Addition Date' ,auto_now=True)
    images = models.ImageField(verbose_name='Image' ,upload_to=image_upload,null=True)
    category = models.ForeignKey(Category,verbose_name='Category' , on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer,verbose_name="Offer",on_delete=models.PROTECT,null=True,blank=True)
    offer_price = models.IntegerField(verbose_name=("Offer Price"),null=True,blank=True)
    
    def save(self,*args, **kwargs):
        if self.offer:
            self.offer_price=self.price-((self.offer.ratio/100)*self.price)
        if self.stock <0:
            self.stock=0
        super(Product,self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return str(self.name)

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