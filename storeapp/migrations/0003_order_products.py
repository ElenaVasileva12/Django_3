# Generated by Django 4.2.7 on 2023-11-28 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_remove_order_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='storeapp.product'),
        ),
    ]
