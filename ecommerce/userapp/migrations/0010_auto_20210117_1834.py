# Generated by Django 3.1.3 on 2021-01-17 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_order_is_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_complete',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
