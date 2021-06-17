from django.contrib import admin
from . models import Address, Cart, CartItem, Customer, Otp

# Register your models here.
    
admin.site.register(Customer)
admin.site.register(Otp)
admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(CartItem)
