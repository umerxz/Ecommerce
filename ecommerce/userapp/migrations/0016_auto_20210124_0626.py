# Generated by Django 3.1.3 on 2021-01-24 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0015_auto_20210123_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
    ]
