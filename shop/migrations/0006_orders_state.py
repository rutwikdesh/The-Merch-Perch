# Generated by Django 3.2 on 2021-05-26 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='state',
            field=models.CharField(default='', max_length=111),
        ),
    ]
