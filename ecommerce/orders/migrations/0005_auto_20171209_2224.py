# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_productpurchase_productpurchasemanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductPurchaseManager',
        ),
        migrations.RemoveField(
            model_name='productpurchase',
            name='user',
        ),
        migrations.AddField(
            model_name='productpurchase',
            name='order_id',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
    ]
