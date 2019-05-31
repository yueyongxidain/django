# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class goodlist(models.Model):
    #商品名称(default=1,)
    goodName = models.CharField(max_length=100,default='')
    #商品价格
    goodPrice = models.FloatField(default=0.00)
    #商品类型
    goodType = models.IntegerField(default=1)
    #商品类型
    goodIsNew = models.BooleanField(default=True)
    #商品描述
    goodDesc = models.TextField(null=True,blank=True,default='')
    #商品简介
    goodBrief = models.TextField(null=True,blank=True,default='')
    #商品封面图
    goodCover = models.CharField(max_length=300,default='')
    #上架
    isOnsale = models.BooleanField(default=False)
    #L库存量
    LinventoryNum = models.IntegerField(default=1)
    #X库存量
    XLinventoryNum = models.IntegerField(default=1)
    # XL库存量
    XLLinventoryNum = models.IntegerField(default=1)
    # XXL库存量
    XXLLinventoryNum = models.IntegerField(default=1)
    #已售量
    salesVolume = models.IntegerField(default=0)
    #收藏量
    collectionNum = models.IntegerField(default=1)
    #是否为平台
    platform = models.IntegerField(default=0)
    #创建时间
    createTime = models.DateTimeField(auto_now_add=True)
    #支持退货日期
    returnTime = models.IntegerField(default=0)
    class Meta:
        db_table = 'goodlist'

