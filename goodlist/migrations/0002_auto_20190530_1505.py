# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-30 15:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goodlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodlist',
            name='LinventoryNum',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='goodlist',
            name='XLinventoryNum',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='goodlist',
            name='XXLLinventoryNum',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='goodlist',
            name='collectionNum',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='goodlist',
            name='createTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goodlist',
            name='goodDesc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='goodlist',
            name='goodImageId',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='goodlist',
            name='isOnsale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='goodlist',
            name='platform',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='goodlist',
            name='returnTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='goodlist',
            name='salesVolume',
            field=models.IntegerField(default=0),
        ),
    ]
