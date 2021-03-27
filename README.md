# 这是一个数据收集web项目

### 由`Tangkz`与`QingFeng`合作完成

### 该项目发布在`www.gitee.com/tangkz/tang-long.git`

## 项目介绍

###

###

## 项目结构

###

###

## 简单的使用方法：

### *	for Linux
克隆项目到本地

	git clon git@gitee.com:Tangkz/tang-long.git	
进入项目目录

	cd ./tang-long	
给与脚本可执行权限

	sudo chmod 755 run.sh	
执行脚本

	./run.sh	
没有权限就加 sudo



### *	for windowns
创建`pythonenv`虚拟环境

	git clon git@gitee.com:Tangkz/tang-long.git
	
使用`pip`安装第三方依赖

	pip install django
	
修改`settings.example.py`文件为`settings.py`

运行`migrate`命令，创建数据库和数据表

	python manage.py migrate
	
启动服务器

	python manage.py runserver




