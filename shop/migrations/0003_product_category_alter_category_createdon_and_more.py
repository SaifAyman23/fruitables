# Generated by Django 5.0.4 on 2024-04-12 18:43

import django.db.models.deletion
import shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_category_isavailable'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='createdOn',
            field=models.DateField(auto_now=True, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='category',
            name='isAvailable',
            field=models.BooleanField(default=True, verbose_name='Is Available'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='addedOn',
            field=models.DateField(auto_now=True, verbose_name='Addition Date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(upload_to=shop.models.image_upload, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Product Name'),
        ),
    ]
