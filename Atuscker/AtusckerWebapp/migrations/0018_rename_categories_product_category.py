# Generated by Django 5.0.6 on 2024-07-06 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AtusckerWebapp', '0017_product_categories_delete_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categories',
            new_name='category',
        ),
    ]