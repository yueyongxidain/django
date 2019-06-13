# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from qiniu import Auth, put_file, etag
from rest_framework import status
import qiniu.config
from django.shortcuts import render
from rest_framework.decorators import api_view
from common.jsonResponse import JsonResponse
from rest_framework.request import Request
import os
import tempfile
# Create your views here.

@api_view(['POST'])
def getImgurl(request):
    if isinstance(request, Request) == False:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
    if request.method == 'POST':
        myFile=request.FILES.get('upload_file',None)
        #需要填写你的 Access Key 和 Secret Key
        access_key = 'aMDZv5nfw4FAd7SKj1NtF3-Z8eClmndPE7drLR7p'
        secret_key = 'OLy8QvMoAFYOAfOBNjmF6vR9KPZUo3NQeOUiTLv2'
        #构建鉴权对象
        q = Auth(access_key, secret_key)
        #要上传的空间
        bucket_name = 'yueyong'
        key = request.data['original_filename']
        # 生成上传 Token，可以指定过期时间等
        token = q.upload_token(bucket_name, key)
        destination = open(os.path.join("E:\\upload", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        ret, info = put_file(token, key, os.path.join("E:\\upload", myFile.name))
        os.remove(os.path.join("E:\\upload", myFile.name))
        if ret['key'] == key:
            print(ret)
            return JsonResponse(success=True,msg="上传成功",file_path='http://pt0pob1av.bkt.clouddn.com/'+ret['key'],code=0,content_type='application/json')

        else:
            return JsonResponse(success=True,msg="上传失败",file_path='http://pt0pob1av.bkt.clouddn.com/'+ret['key'], code=0, content_type='application/json')

    else:
        return JsonResponse(msg='请求方式出错',code=0,content_type='application/json')



