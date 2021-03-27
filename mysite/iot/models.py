
# iot/models.py

from django.db import models
# timezone 用于处理时间相关事务。
from django.utils import timezone


# 温度数据模型
class RaspberryPi(models.Model):
    temperature = models.FloatField()
    weight = models.FloatField()
    bmp = models.IntegerField()
    iir = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)
    
    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        return self.title


class Book(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    publish = models.DateTimeField(default=timezone.now)
    bio = models.CharField(max_length=200)
    class Meta:
        ordering = ('-publish',)


class Music(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    publish = models.DateTimeField(default=timezone.now)
    path = models.FilePathField()
    bio = models.CharField(max_length=200)
    class Meta:
        ordering = ('-publish',)


class Film(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    publish = models.DateTimeField(default=timezone.now)
    path = models.FilePathField()
    bio = models.CharField(max_length=200)
    class Meta:
        ordering = ('-publish',)





