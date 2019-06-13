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
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filter import GoodsFilter
# Create your views here.

#获取商品列表
@api_view(['POST'])
def getList(request):
    if isinstance(request, Request) == False:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST,content_type='application/json')
    if request.method == 'POST':
        filter_backends = (DjangoFilterBackend)
        goods = goodlist.objects.all().order_by('-createTime')
        #过滤
        data = GoodsFilter(request.data,queryset=goods).qs
        totle = len(goodlistSerializer(data,many=True).data)
        #分页
        page = MyPageNumberPagination()
        page_roles = page.paginate_queryset(queryset=data, request=request)
        #序列化
        serializer = goodlistSerializer(page_roles,many=True)
        serializer.data.desc = None
        return JsonResponse({'data':serializer.data,'totle':totle},code=0,content_type='application/json')

#新增商品列表
@api_view(['POST'])
def addList(request):
    if isinstance(request, Request) == False:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
    if request.method == 'POST':
        if not request.data:
            return JsonResponse(status=status.HTTP_200_OK, msg='参数不允许为空',content_type='application/json')
        else:
            if 'id' in request.data:
                goods = goodlist.objects.get(id=request.data['id'])
                serializer = goodlistSerializer(data=goods)
                serializer.update(instance=goods, validated_data=request.data)
                return JsonResponse(status=status.HTTP_200_OK, code=0, content_type='application/json')
            else:
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

# 删除商品列表
@api_view(['POST'])
def deleteList(request):
    if isinstance(request, Request) == False:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
    if request.method == 'POST':
        if not request.data:
            return JsonResponse(status=status.HTTP_200_OK, msg='参数不允许为空', content_type='application/json')
        else:
            if 'id' in request.data:
                goodlist.objects.get(id = request.data['id']).delete()
                return JsonResponse(code=0, content_type='application/json')
            else:
                return JsonResponse(status=status.HTTP_200_OK, msg='参数不允许为空', content_type='application/json')

