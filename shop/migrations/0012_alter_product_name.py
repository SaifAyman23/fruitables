# Generated by Django 5.0.4 on 2024-04-12 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Product Name'),
        ),
    ]