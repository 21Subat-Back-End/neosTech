from django.db import models

# Create your models here.

class Brand(models.Model):
    title =models.CharField(("Marka Adı"), max_length=50)
    
    def __str__(self) -> str:
        return self.title

class ProductStorage(models.Model):
    title = models.CharField(("Ürün Hafızası"), max_length=50)
    
    def __str__(self) -> str:
        return self.title
    
class ProductColor(models.Model):
    title = models.CharField(("Ürün Rengi"), max_length=50)

    def __str__(self) -> str:
        return self.title
    
class Product(models.Model):
    productBrand = models.ForeignKey(Brand, verbose_name=("Marka Adı"), on_delete=models.CASCADE,null=True,blank=True)
    productTitle = models.CharField(("Ürünün Başlığı"), max_length=50)
    productDesct = models.TextField(("Ürünün Açıklaması"))
    productImg = models.ImageField(("Ürünün Fotoğrafı"), upload_to=None, height_field=None, width_field=None, max_length=None)
    productColor = models.ForeignKey(ProductColor, verbose_name=("Renk"), on_delete=models.CASCADE,null=True,blank=True)
    productStorage = models.ForeignKey(ProductStorage, verbose_name=("Hafıza"), on_delete=models.CASCADE,null=True,blank=True)
    productStock = models.PositiveIntegerField(("Stok Durumu"),null=True,blank=True)
    productPrice = models.PositiveIntegerField(("Ürünün Fiyatı"))

    def __str__(self) -> str:
        return self.productTitle
    