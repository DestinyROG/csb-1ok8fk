# Generated by Django 4.1.5 on 2023-02-19 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewApp', '0006_alter_cart_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner_image',
            name='category',
            field=models.CharField(choices=[('fashions', 'fashions')], max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('fashions', 'fashions')], max_length=255),
        ),
    ]
