# Generated by Django 5.0.6 on 2024-06-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AtusckerWebapp', '0007_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='productdescription',
        ),
        migrations.RemoveField(
            model_name='product',
            name='productname',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='imageAlt',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='productimage',
            name='imageSrc',
            field=models.URLField(blank=True, max_length=255),
        ),
    ]
