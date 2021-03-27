"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from learn import views as learn_views
# 消息通知
import notifications.urls

urlpatterns = [
    # 后台
    path('admin/', admin.site.urls),
    # 主页
    path('',learn_views.index),
    # 我的物联网项目
    path('iot/', include('iot.urls', namespace='iot')),
    # 供学习使用
    path('learn/', include('learn.urls', namespace='learn')),
    # 文章管理
    path('article/', include('article.urls', namespace='article')),
    # 用户管理
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    # 密码重置
    path('password-reset/', include('password_reset.urls')),
    # 文件下载
    path('download/<path:path>/',learn_views.downloadfile, name="download"),
    # 消息通知
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    # notice
    path('notice/', include('notice.urls', namespace='notice')),
    # 第三方登录
    # path('accounts/', include('allauth.urls')),
]

# 为以后上传的图片配置好了URL路径
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)














