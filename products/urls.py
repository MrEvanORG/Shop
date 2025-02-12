from django.urls import path , include
from . import views
from django.contrib import admin

urlpatterns = [
    path('',views.homepage,name='home'),
    path('products/',views.view_products,name='products'),
    path('buy-product/<int:pid>/',views.buy_product,name='buy-product'),
    path('confirm_buy/',views.confirm_buy,name='confirm'),
    path('order-product/',views.order_product,name='order-product'),
    path('farmer_regsiter/',views.farmer_register,name='farmer-register'),
    path('about-us/',views.about_us,name='about-us'),
]
