# Generated by Django 3.1.3 on 2021-01-22 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0014_auto_20210120_2214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='stock',
        ),
    ]
