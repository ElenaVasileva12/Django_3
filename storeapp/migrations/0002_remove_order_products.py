# Generated by Django 4.2.7 on 2023-11-28 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
    ]
