# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodlist', '0004_auto_20190531_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodlist',
            name='goodIsNew',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='goodlist',
            name='goodType',
            field=models.IntegerField(default=1),
        ),
    ]
