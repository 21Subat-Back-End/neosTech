"""
URL configuration for neosTech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from article.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='anasayfa'),
    path('detay/<id>/',detail,name='detay'),
    path('marka/<id>/',brand,name='marka'),
    path('girisyap/',loginn,name='girisyap'),
    path('kayıtol/',register,name='kayıtol'),
    path('cıkıs/',logoutt,name='cıkıs'),
    path ('sepet/', sepet ,name='sepet'),
    path('urunekle/<id>/',urunekle,name="urunekle"),
    path('urunsil/<id>/',urunsil,name="urunsil"),
    path('urunguncelle/<id>/',urunGüncelle,name="urungüncelle")
    
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
