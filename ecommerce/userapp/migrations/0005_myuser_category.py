# Generated by Django 3.1.3 on 2021-01-14 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_auto_20210104_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='category',
            field=models.CharField(choices=[('W', 'Women'), ('M', 'Men'), ('K', 'Kid')], default='null', max_length=5),
        ),
    ]
