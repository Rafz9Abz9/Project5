from django.contrib import admin

from .models import  CustomUser, ShippingAddress


admin.site.register(CustomUser)
admin.site.register(ShippingAddress)
