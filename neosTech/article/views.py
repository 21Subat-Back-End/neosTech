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
    comment = Comment.objects.filter(productComment=product)
    
    if request.method == 'POST':
        comment = request.POST['comment']
        com = Comment(commentText=comment,user=request.user)
        com.save()
    
    context = {
        'product':product,
        'productcolor':productcolor,
        'productstorage':Productstorage,
        'comment':comment
    }
    
    return render (request,'detay.html',context)

def brand (request,id):
    
    brand = Product.objects.filter(productBrand=id)
    
    context = {
        'brand':brand
    }
    
    return render (request,'brand.html',context)

def register(request):
    return render(request,'part/register.html')


def loginn(request):
    return render(request,'part/login.html')
