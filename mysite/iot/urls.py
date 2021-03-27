
# iot/urls.py

# 引入path
from django.urls import path
# 引入views.py
from . import views

# 正在部署的应用的名称
app_name = 'iot'

urlpatterns = [
    path('index/', views.index, name='index'),
    
    
]