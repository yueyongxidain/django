# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class imglist(models.Model):
    #图片对应的类型ID
    sourceId = models.IntegerField()
    #图片所属类型
    sourceType = models.IntegerField()
    #图片路径
    imgPath = models.CharField(max_length=300,null=True)
    #图片名称
    imgName = models.CharField(max_length=100,null=True)
    #创建时间
    createTime = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'imglist'