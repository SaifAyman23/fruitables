# Generated by Django 5.0.4 on 2024-04-29 16:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0031_remove_cart_product_remove_cart_user_delete_coupon_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon', models.CharField(max_length=50, verbose_name='Coupon')),
                ('ratio', models.IntegerField(verbose_name='Ratio')),
                ('created_at', models.DateField(auto_now=True, verbose_name='Created at')),
                ('expiry_date', models.DateField(null=True, verbose_name='Expires at')),
                ('is_available', models.BooleanField(default=True, verbose_name='Is Available')),
            ],
            options={
                'verbose_name': 'Coupon',
                'verbose_name_plural': 'Coupons',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Price')),
                ('total', models.IntegerField(blank=True, null=True, verbose_name='Total')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
            },
        ),
    ]
