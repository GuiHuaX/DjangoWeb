# -*- coding: utf-8 -*-
# learn/views.py

from django.shortcuts import render
from django.shortcuts import HttpResponse

from django.http import FileResponse
from django.http import StreamingHttpResponse
from django.http import HttpResponseRedirect

import os
from django.conf import settings 


# 视图函数
def index(request):
    context = { 
       
    }
    # render函数：载入模板，并返回context对象
    return render(request, 'home.html', context)


def info(request):
    context = {
    
    }
    return render(request, 'info.html', context)


def downloadfile(request,path):
    # file_name = request.GET["file"]
    
    file_path = os.path.join(settings.BASE_DIR,path)    # 下载文件的绝对路径
    print(file_path)
    
    if not os.path.isfile(file_path):  # 判断下载文件是否存在
        return HttpResponse("Sorry but Not Found the File") # 不存在
    
    def file_iterator(file_path, chunk_size=512):
        """
        文件生成器,防止文件过大，导致内存溢出
        :param file_path: 文件绝对路径
        :param chunk_size: 块大小
        :return: 生成器
        """
        with open(file_path, mode='rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    try:
        response = StreamingHttpResponse(file_iterator(file_path))
        # response = HttpResponse(open(file_path, 'rb'))
        # response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(file_name)
    except:
        return HttpResponse("Sorry but Not Found the File")
    
    return response
    
    
    
    
    
    
    
    