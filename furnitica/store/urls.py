from django.urls import path
from . import views

urlpatterns = [
path('', views.ad_login, name='ad_login'),
path ('ad_home', views. ad_home, name = 'home'),
path('ad_user', views.ad_user, name = 'usermanage' ),
path('ad_product', views.ad_product, name ='productmanage'),
path('ad_order', views.ad_order, name= 'ordermanage'),
path('ad_offer', views.ad_offer, name= 'offermanage'),
path('ad_category', views.ad_category, name = 'categorymanage'),
path('newcategory', views.newcategory, name = 'newcategory'),
path('editcategory/<id>', views.editcategory, name = 'editcategory'),
path('deletecategory/<id>', views.deletecategory, name = 'deletecategory'),
path('delete_cat/<id>', views.delete_cat, name='delete_cat'),
path('nodeletecat/<id>', views.nodelete_cat, name="nodeletecat"),
path('newproduct', views.newproduct, name='newproduct'),
path('editproduct/<id>', views.editproduct, name='editproduct'),
path('deleteproduct/<id>', views.deleteproduct, name = 'deleteproduct'),
path('delete_pro/<id>', views.delete_pro, name='delete_pro'),
path('nodeletepro/<id>', views.nodelete_pro, name="nodeletepro"),
path('block/<id>', views.block, name = 'block'),
path('ad_home', views.ad_home, name = 'ad_home'),
path('ad_search', views.ad_search, name='ad_search'),





]