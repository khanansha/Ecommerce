# Generated by Django 2.0.2 on 2020-05-05 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20200505_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quentity',
            field=models.IntegerField(default=1),
        ),
    ]
