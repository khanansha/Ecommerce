# Generated by Django 2.0.2 on 2020-05-05 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_sizes'),
        ('cart', '0004_auto_20200505_1308'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='Cartdatabase',
        ),
    ]