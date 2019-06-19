
# -*- coding: utf-8 -*-

from rest_framework import serializers
from goodlist.models import goodlist
from imglist.models import imglist
from imglist.serializers import imglistSerializer

class goodlistSerializer(serializers.ModelSerializer):
    imgList =  serializers.SerializerMethodField()
    class Meta:
        model = goodlist
        fields ='__all__'
    def get_imgList(self, obj):

        return serializers.serialize("json",imglist.objects.filter(sourceType=0,sourceId=obj.id))
