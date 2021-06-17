from django.urls import path
from . import views

urlpatterns = [path('', views.landing, name= 'landing'),
                path('home', views.home, name= 'home'),
                
                path('register', views.register, name = 'register'),
                path('login', views.login, name = 'login'),
                path('sendotp', views.sendotp, name = 'sendotp'),
                path('signup', views.signup, name = 'signup'),
                path('verify/<str:num>', views.verify, name ='verify'),
                path('logout', views.logout, name = 'logout'),
                path('productdetail/<id>', views.productdetail, name = 'productdetail'),
                path('add_cart/<id>/', views.add_cart, name='add_cart'),
                path('cart', views.cart, name='cart'),
                path('remove_cart/<int:product_id>', views.remove_cart, name='remove_cart'),
                path('remove_cart_item/<id>', views.remove_cart_item, name= 'remove_cart_item'),
                path('my_account', views.my_account, name='my_account'),
                path('signin', views.signin, name='signin'),
                path('checkout', views.checkout, name="checkout"),
                path('address', views.address, name = 'address'),
                
                

]