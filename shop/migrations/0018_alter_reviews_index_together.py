# Generated by Django 5.0.1 on 2024-04-26 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_reviews'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='reviews',
            index_together=set(),
        ),
    ]
