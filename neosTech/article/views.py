from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    
    product= Product.objects.all()
    brand= Brand.objects.all()
    
    
    context = {
        'product':product,
        'brand':brand
    }
    return render(request,'index.html',context)

def detail(request,id):
    
    product = Product.objects.get(id=id)
    productcolor = ProductColor.objects.all()
    Productstorage = ProductStorage.objects.all()
    
    context = {
        'product':product,
        'productcolor':productcolor,
        'productstorage':Productstorage
    }
    
    return render (request,'detay.html',context)