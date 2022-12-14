# Generated by Django 4.1.3 on 2022-12-29 20:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_product_created_at_remove_product_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 12, 29, 20, 59, 33, 855089, tzinfo=datetime.timezone.utc), verbose_name='Дата створення'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата змінення'),
        ),
    ]
