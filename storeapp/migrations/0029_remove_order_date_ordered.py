# Generated by Django 4.2.7 on 2023-12-04 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0028_alter_order_date_ordered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_ordered',
        ),
    ]
