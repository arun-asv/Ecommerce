from django.shortcuts import redirect, render
from .models import Category, Product
from .forms import CategoryForm, ProductForm
from django.http import HttpResponse
from customer.models import Customer
from django.contrib.auth.models import User, auth

# Create your views here.
def ad_login(request):
    return render(request, 'admin/login.html')

def ad_home (request):
    
    # if request.method =='POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = auth.authenticate(username = username, password=password)
    #     if user.is_superuser:
    #         auth.login(request,user)
            return render (request, 'admin/index.html')
        # else:
        #     return redirect('ad_login')
    
        

def ad_user (request):
    
    customers = Customer.objects.all()

    return render(request, 'admin/user/usermanage.html', {'customers': customers})

def ad_product(request):
    
    products = Product.objects.all()

    return render(request, 'admin/product/productmanage.html', {'products': products})

def ad_category(request):
    
    categories = Category.objects.all()

    return render(request, 'admin/category/categorymanage.html', {'categories': categories})

def ad_offer(request):
    return render(request, 'admin/offer/offermanage.html')

def ad_order(request):
    return render(request, 'admin/order/ordermanage.html')

def newcategory(request):
    form = CategoryForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect('categorymanage')
    else:
        form = CategoryForm
        context = {'form': form}
        return render(request, 'admin/category/addcategory.html', context)

def editcategory(request, id):
    categories = Category.objects.get(pk=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance = categories)

        if form.is_valid():
            form.save()
            return redirect('categorymanage')
        
    else:
        form = CategoryForm(instance = categories)
        return render(request, 'admin/category/editcategory.html', {'form': form, 'categories': categories})

def deletecategory(request, id):
    categories = Category.objects.get(pk=id)
    return render (request, 'admin/category/deletecategory.html', {'categories': categories})

def delete_cat(request, id):
    categories = Category.objects.filter(pk=id)
    categories.delete()
    return redirect ('categorymanage')

def nodelete_cat(request, id):
    categories = Category.objects.all()

    return render(request, 'admin/category/categorymanage.html', {'categories': categories})


def newproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            print('working')
            return redirect ('productmanage')
        
    
        
        else:
            form = ProductForm()
            posts = Product.objects.all().order_by('-date_posted')
            return render(request, 'admin/product/addproduct.html', {'form': form, 'posts': posts})
    else:
            form = ProductForm()
            posts = Product.objects.all().order_by('-date_posted')
            return render(request, 'admin/product/addproduct.html', {'form': form, 'posts': posts})
        
    



def editproduct(request, id):
    products = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance = products)

        if form.is_valid():
            form.save()
            return redirect('productmanage')
        
    else:
        form = ProductForm(instance = products)
        return render(request, 'admin/product/editproduct.html', {'form': form, 'products': products})

def deleteproduct(request, id):
    products = Product.objects.get(pk=id)
    return render (request, 'admin/product/deleteproduct.html', {'products': products })

def delete_pro(request, id):
    products = Product.objects.filter(pk=id)
    products.delete()
    return redirect ('productmanage')

def nodelete_pro(request, id):
    products = Product.objects.all()

    return render(request, 'admin/product/productmanage.html', {'products': products})


def block(request, id):
    user = Customer.objects.get(pk=id)
    user.is_active  = not (user.is_active)
    user.save()
    return redirect('usermanage')


def ad_search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        users = Customer.objects.filter(firstname__contains = searched)
        return render (request, 'admin/user/usermanage.html', {'searched': searched, 'users': users})
    else:
        return redirect('ad_home')

        












            

