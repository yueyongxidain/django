
# -*- coding: utf-8 -*-

from rest_framework import serializers
from goodlist.models import goodlist
from imglist.models import imglist
from django.core.serializers import serialize
from imglist.serializers import imglistSerializer

class goodlistSerializer(serializers.ModelSerializer):
    imgList =  serializers.SerializerMethodField()
    class Meta:
        model = goodlist
        fields ='__all__'
    def get_imgList(self, obj):
        result = imglist.objects.filter(sourceType=0,sourceId=obj.id)
        return imglistSerializer(result,many=True).data
