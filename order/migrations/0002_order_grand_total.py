# Generated by Django 5.0.1 on 2024-04-28 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='grand_total',
            field=models.FloatField(null=True),
        ),
    ]
