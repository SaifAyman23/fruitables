from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(OrderProduct)
class ModelAdmin(admin.ModelAdmin):
    list_display=['order','id']
@admin.register(Order)
class ModelAdmin(admin.ModelAdmin):
    list_display=['first_name','id']