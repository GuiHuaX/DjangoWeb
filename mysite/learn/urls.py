
# learn/urls.py

# 引入path
from django.urls import path
# 引入views.py
from . import views

# 正在部署的应用的名称
app_name = 'learn'

urlpatterns = [
    path('home/', views.index, name='home'),
    path('info/', views.info, name='info'),
]