# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodlist', '0005_auto_20190531_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodlist',
            name='goodBrief',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]