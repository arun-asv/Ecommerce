from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from store.models import Product, Category
from . models import Customer, Otp, CartItem, Cart
from django.contrib import messages
from .forms import AddressForm
from .models import Address

# Create your views here.

def register (request):
    return render (request, 'user/user-register.html')

def login (request):
    return render (request, 'user/user-login.html')


def home (request):
    if request.session.has_key('username'):
        queryset = Product.objects.all()
        querycat = Category.objects.all()
        context = {'products': queryset, 'categories': querycat}
        return render(request, 'user/home.html', context)
    else:
        return redirect('landing')
    
    
def productdetail(request, id):
    if request.session.has_key('username'):
        product = Product.objects.get(pk = id)
        return render(request, 'user/product-detail.html', {'product': product})
    else:
        return redirect('landing')



def landing (request):
    queryset = Product.objects.all()
    querycat = Category.objects.all()
    context = {'products': queryset, 'categories': querycat}
    return render(request, 'user/index.html', context)

def sendotp(request):
    if request.method =='POST':
        num = request.POST['number']
        user = Customer.objects.get(number = num)
        if user.is_active:
            request.session['username'] = user.firstname
            send = Otp.objects.create(num = num)
            send.save()
            return render (request, 'user/otp.html', {'num' : num})
        else:
            messages.error (request, 'This phone number is not registered', extra_tags=sendotp)
            return redirect ('login')

def verify (request, num):
    if request.method =='POST':
        otp = request.POST['otp']
        votp = Otp.objects.get(num = num)
        if votp.checkotp(otp):
            user = Customer.objects.get(number = num)
            votp.delete()
            request.session['username'] = user.username
            return redirect('home')
        
        else:
            return redirect ('login')

def signin(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = Customer.objects.get(username = username, password = password)
        if user.is_active:
                request.session['username']= user.username
                return redirect ('home')
        
        else: 
            return redirect ('login')
    
    else:
        return redirect('login')


def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        number = request.POST['number']

        if password1 == password2:
            if Customer.objects.filter(email=email).exists():
                messages.error(request, 'email already exists', extra_tags ='signup')
                return redirect('register')
            elif Customer.objects.filter(username = username).exists():
                 messages.error(request, 'username already exists', extra_tags ='signup')
            
            elif Customer.objects.filter(number=number).exists():
                messages.error(request, 'mobile number already exists', extra_tags='signup')
                return redirect ('register')
            

            else:
                user = Customer.objects.create(password=password1, email=email, firstname=firstname, lastname=lastname, number=number, username = username)
                print ('saved')
                user.save()
                request.session['username'] = user.username
                return redirect ('home')
        else:
            messages.error(request, 'password does not match', extra_tags ='signup')
            return redirect('register')

def logout(request):
    if request.session.has_key('username'):
        request.session.flush()
        return redirect('landing')
    else:
        return redirect ('home')



def _cart_id(request):

    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request,id):
    product = Product.objects.get(id = id)
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get (product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )
        cart_item.save()
    return redirect('cart')

        

def cart(request, total = 0, quantity =0, cart_item = None):
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active = True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

    
    except ObjectDoesNotExist:
        pass

    context = {
        'total' : total,
        'quantity': quantity,
        'cart_items': cart_items,
    }
    return render (request, 'user/product-cart.html', context)


def remove_cart (request,product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def remove_cart_item(request, id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product,id = id)
    cart_item = CartItem.objects.get(product = product, cart=cart)
    cart_item.delete()
    return redirect('cart')

def my_account(request):
    if request.session.has_key('username'):
        uname = request.session['username']
        user = Customer.objects.get(username = uname)
        return render(request, 'user/user-account.html', {'user': user})
    else:
        return redirect('landing')



def checkout(request, total=0, quantity = 0, cart_items=None):
    if request.session.has_key('username'):
        
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
            for cart_item in cart_items:
                total +=(cart_item.product.price * cart_item.quantity)
                quantity += cart_item.quantity
            
        except ObjectDoesNotExist:
            pass


        form = AddressForm()
       
        
    
        uname = request.session['username']
        user = Customer.objects.get(username = uname)
        queryset = Address.objects.all().filter(user = user)

        context = {
            'total' : total,
            'form' : form,
            'quantity': quantity,
            'cart_items': cart_items,
            'addresses' : queryset


        }

    
        return render(request, 'user/product-checkout.html', context)
    else:
        return redirect('landing')


def address(request):
    if request.session.has_key('username'):
        if request.method == 'POST':
            form = AddressForm(request.POST)

            if form.is_valid():
                newaddress = form.save(commit=False)
                uname = request.session['username']
                user = Customer.objects.get(username = uname)

                newaddress.user = user
                newaddress.save()
                return redirect('checkout')
        else:
            form = AddressForm
            context = {'form': form}
            return render(request, 'user/product-checkout.html', context)
    else:
        return render('landing')