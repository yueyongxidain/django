# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodlist', '0006_goodlist_goodbrief'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodlist',
            name='goodCover',
            field=models.CharField(default='', max_length=300),
        ),
    ]
