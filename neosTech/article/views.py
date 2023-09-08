from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db.models import Q


# Create your views here.

def index(request):
    
    product= Product.objects.all()
    brand= Brand.objects.all()
    
    query= request.GET.get('q')
    if query:
        product=product.filter(
            Q(productTitle__icontains=query)|
            Q(productDesct__icontains=query)|
            Q(productBrand__title__icontains=query)|
            Q(productColor__title__icontains=query)
        ).distinct
    
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
        com = Comment(commentText=comment,productComment=product,user=request.user)
        com.save()
        
        return redirect('/detay/' + id + '/')

    
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
    
    if request.method =='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password==password2:
            if User.objects.filter(username=firstname).exists():
                context = {
                    'information':'Böyle bir kullanıcı mevcut farklı bir kullanıcı adı deneyiniz.'
                }
                
                return render(request,'part/register.html',context)
            
            if User.objects.filter(email=email).exists():
                context={
                    'information':'Sisteme kaydetmek istediğiniz e-posta adresi farklı bir kullanıcımız tarafından kullanılıyor.'
                }
                
                return render(request,'part/register.html',context)

            else:
                user = User.objects.create_user(username=firstname,first_name=firstname, last_name=lastname,email=email,password=password)
                user.save()
                
                context={
                    'success':'Bilgileriniz sisteme kaydedildi. Kullanıcı ve şifrenizle giriş yapabilirsiniz.'
                }
                
                return render(request,'part/register.html',context)
        else:
            context = {
                'information':'Parolanız tekrar parolanızla uyuşmuyor. Tekrar kayıt olmayı deneyin'
            }
            
            return render(request,'part/register.html',context)
    
    return render(request,'part/register.html')


def loginn(request):
    
    if request.method =='POST':
        username=request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            user is not None
            login(request,user)
            return redirect('anasayfa')
        else:
            context={
                'information':'Girmiş bilgiler hatalı görünüyor tekrar deneyin.'
            }
            return render(request,'part/login.html',context)
    
    return render(request,'part/login.html')

def logoutt (request):
    
    logout(request)
    
    return redirect('anasayfa')


def urunekle(request, id):
    product= Product.objects.get(id=id)
    user =request.user
    sepet = Sepet.objects.create(product=product,user=user,adet=1,allprice=product.productPrice)
    sepet.save()
    return redirect('sepet')

def sepet(request):
    sepet =Sepet.objects.filter(user=request.user)
    toplam=0
    
    for item in sepet:
        toplam+=item.product.productPrice * item.adet
    
    context = {
        'sepet':sepet,
        'toplam':toplam
    }
    
    return render(request,'shopping.html',context)