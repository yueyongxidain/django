
# -*- coding: utf-8 -*-

from rest_framework import serializers
from imglist.models import imglist

class imglistSerializer(serializers.ModelSerializer):


    class Meta:
        model = imglist
        fields ='__all__'
