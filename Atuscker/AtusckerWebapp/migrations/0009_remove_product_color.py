# Generated by Django 5.0.6 on 2024-06-09 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AtusckerWebapp', '0008_remove_product_productdescription_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
    ]
