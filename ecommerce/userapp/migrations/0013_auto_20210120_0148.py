# Generated by Django 3.1.3 on 2021-01-19 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0012_auto_20210117_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
