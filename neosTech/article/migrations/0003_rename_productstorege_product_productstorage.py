# Generated by Django 4.2.1 on 2023-08-31 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_product_productstock_product_productstorege_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productStorege',
            new_name='productStorage',
        ),
    ]
