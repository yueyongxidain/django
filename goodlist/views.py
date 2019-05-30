# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import render
from goodlist.models import goodlist
from goodlist.serializers import goodlistSerializer
# Create your views here.

#获取商品列表
@api_view(['GET'])
def getList(request):
    if isinstance(request, Request) == False:
        return Response( status=status.HTTP_400_BAD_REQUEST,content_type='application/json')
    if request.method == 'GET':
        print request.query_params
        goods = goodlist.objects.all()
        serializer = goodlistSerializer(goods)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = goodlistSerializer(data=request.data)   #反序列
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED,content_type='application/json')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,content_type='application/json')