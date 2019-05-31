# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.decorators import api_view
from common.jsonResponse import JsonResponse
from rest_framework.request import Request
from django.shortcuts import render
from goodlist.models import goodlist
from goodlist.serializers import goodlistSerializer
from common.MyPageNumberPagination import MyPageNumberPagination
# Create your views here.

#获取商品列表
@api_view(['POST'])
def getList(request):
    if isinstance(request, Request) == False:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST,content_type='application/json')
    if request.method == 'POST':
        goods = goodlist.objects.filter(isOnsale= (request.data['isOnsale'] if( request.data.has_key('isOnsale')) else False))
        page = MyPageNumberPagination()
        page_roles = page.paginate_queryset(queryset=goods, request=request)
        serializer = goodlistSerializer(page_roles,many=True)
        serializer.data.desc = None
        return JsonResponse(serializer.data,code=0,content_type='application/json')

#新增商品列表
@api_view(['POST'])
def addList(request):
    if isinstance(request, Request) == False:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
    if request.method == 'POST':
        print any(request.data)
        if not any(request.data):
            return JsonResponse(status=status.HTTP_200_OK, msg='参数不允许为空',content_type='application/json')
        serializer = goodlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(status=status.HTTP_200_OK, code=0,content_type='application/json')
        else:
            return JsonResponse(serializer.errors,status=status.HTTP_200_OK, msg='新增参数错误', content_type='application/json')
#获取商品详情
@api_view(['GET'])
def getdetail(request):
    if isinstance(request, Request) == False:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
    if request.method == 'GET':
        params =  request.query_params.dict()
        if params.has_key('id'):
            goods = goodlist.objects.filter(id = params['id'])
            serializer = goodlistSerializer(goods,many=True)
            return JsonResponse(serializer.data, code=0, content_type='application/json')