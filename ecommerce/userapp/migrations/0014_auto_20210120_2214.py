# Generated by Django 3.1.3 on 2021-01-20 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0013_auto_20210120_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
    ]
