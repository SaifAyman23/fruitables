from django.db import models

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
    images = models.ImageField(verbose_name='Image' ,upload_to=image_upload)
    category = models.ForeignKey(Category,verbose_name='Category' , on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.name).capitalize()
    

# class Review(models.Model):
#     user=