
# 导入 HttpResponse 模块
from django.http import HttpResponse
from django.shortcuts import render



# 视图函数
def index(request):
  
    # render函数：载入模板，并返回context对象
    return render(request, 'iot/index.html')