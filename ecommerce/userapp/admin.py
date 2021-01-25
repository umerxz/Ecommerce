# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Product,Order,MyUser,Item

admin.site.register(MyUser)

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Item)
