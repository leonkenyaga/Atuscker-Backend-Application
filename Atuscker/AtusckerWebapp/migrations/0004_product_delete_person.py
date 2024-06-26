# Generated by Django 5.0.6 on 2024-06-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AtusckerWebapp', '0003_remove_person_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100)),
                ('productdescription1', models.CharField(max_length=200)),
                ('productdescription2', models.CharField(max_length=200)),
                ('productnumber', models.IntegerField()),
                ('productimage', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
