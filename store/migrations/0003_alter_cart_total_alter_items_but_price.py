# Generated by Django 4.2.6 on 2024-12-13 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_cart_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='items',
            name='but_price',
            field=models.IntegerField(default=0),
        ),
    ]