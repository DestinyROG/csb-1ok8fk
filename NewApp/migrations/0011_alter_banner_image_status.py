# Generated by Django 4.1.5 on 2023-02-19 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewApp', '0010_alter_banner_image_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner_image',
            name='status',
            field=models.CharField(blank=True, choices=[('Active', 'active'), ('Non-Active', '')], max_length=150),
        ),
    ]
