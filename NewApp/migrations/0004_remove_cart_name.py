# Generated by Django 4.1.5 on 2023-02-18 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewApp', '0003_banner_image_cart_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='name',
        ),
    ]
