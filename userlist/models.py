# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class userlist(models.Model):
    #微信返回的用户UID
    uId = models.CharField(max_length=300,null=True)
    #电话
    telphone = models.CharField(max_length=11,null=True)
    # 创建时间
    createTime = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'userlist'


class addresslist(models.Model):
    #UID  对应用户UID
    uId =  models.CharField(max_length=300,null=True)
    #省
    province = models.CharField(max_length=300,null=True)
    #市
    city = models.CharField(max_length=300,null=True)
    #区
    area = models.CharField(max_length=100,null=True)
    #详细地址
    detailedddressd=models.CharField(max_length=300,null=True)
    #创建时间
    createTime = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'addresslist'