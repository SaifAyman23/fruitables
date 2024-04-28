from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','id']
admin.site.register(Offer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Coupon)
admin.site.register(Reviews)