# Generated by Django 4.2.1 on 2023-08-31 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_rename_productstorege_product_productstorage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Marka Adı')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='productBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.brand', verbose_name='Marka Adı'),
        ),
    ]