
# -*- coding: utf-8 -*-

from rest_framework import serializers
from goodlist.models import goodlist

class goodlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = goodlist
        fields = '__all__'
