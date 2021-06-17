from django.db import models
from django.db.models.deletion import CASCADE
from twilio.rest import Client
import random
from store.models import Product


# Create your models here.

class Customer(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200) 
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=50)
    number = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    username = models.CharField(max_length=100)
    
    
    

    def __str__(self):
        return self.firstname


class Otp(models.Model):
    num = models.IntegerField()
    validnum = random.randint(1000, 9999)
    vnum = validnum

    def __str__(self):
        return self.num

    def save(self, *args, **kwargs):
        if self.num is not None:
            account_sid = 'ACd7fa104b699c9fc0b3576c97ad67ec4c'
            auth_token = '265ae0f651a5c215a47fcafc3db219c2'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                        body=f'OTP for Login - {self.validnum}',
                                        from_='+18173187537',
                                        to='+91' +self.num
                                    )

            print(message.sid)
        return super().save(*args, **kwargs)

    def checkotp(self,otp):
        if str(self.vnum) ==otp:
            return True
        else:
            return False


class Cart(models.Model):
    cart_id = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)

    def __str__ (self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product


class Address(models.Model):
    user = models.ForeignKey(Customer, on_delete=CASCADE)
    fullname = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    mobile = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    landmark = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    
    def __str__(self):
        return self.fullname

    

    
        

    





    
    


    
    


    
