# Generated by Django 2.0.2 on 2020-04-23 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200420_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='', upload_to='product/images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='products.Product')),
            ],
        ),
    ]
