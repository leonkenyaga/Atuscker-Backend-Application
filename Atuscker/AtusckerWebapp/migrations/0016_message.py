# Generated by Django 5.0.6 on 2024-07-06 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AtusckerWebapp', '0015_product_offer_product_offerfrom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AtusckerWebapp.categories')),
            ],
        ),
    ]