# Generated by Django 5.0.6 on 2024-06-07 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AtusckerWebapp', '0006_rename_productdescription1_product_productdescription_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='files/product_images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AtusckerWebapp.product')),
            ],
        ),
    ]
