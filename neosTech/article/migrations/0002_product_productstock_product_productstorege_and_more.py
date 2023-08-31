# Generated by Django 4.2.1 on 2023-08-31 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productStock',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Stok Durumu'),
        ),
        migrations.AddField(
            model_name='product',
            name='productStorege',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.productstorage', verbose_name='Hafıza'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productColor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.productcolor', verbose_name='Renk'),
        ),
        migrations.AlterField(
            model_name='productcolor',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Ürün Rengi'),
        ),
        migrations.AlterField(
            model_name='productstorage',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Ürün Hafızası'),
        ),
    ]