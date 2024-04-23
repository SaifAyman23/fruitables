from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def profile_upload(instance,filename:str):
    extension = filename.split('.')[1]
    return f'accounts/{instance.user}.{extension}'

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField( upload_to=profile_upload,blank=True)
    phone = models.CharField(max_length=15)

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return str(self.user)
    
    @receiver(post_save,sender=User)
    def created_user(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)