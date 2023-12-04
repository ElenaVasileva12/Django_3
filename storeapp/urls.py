from django.contrib import admin
from django.urls import path,include
from .views import index,view_client

urlpatterns = [
    path('',index,name='index'),     #http://127.0.0.1:8088/store/
    path('client/<int:day_>',view_client,name='client'),
    #path('product/',view_product,name='product'),
    #path('order/',view_order,name='order'),
]
