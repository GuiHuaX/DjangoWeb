
# python 虚拟环境

## 进入新建文的件夹 
	cd django_project

	python -V
## 创建python虚拟环境
	python -m venv env
## 进入python虚拟环境
	env\Scripts\activate.bat
## 退出虚拟环境
	env\Scripts\deactivate.bat

## 安装django
	pip install django
## 创建django项目
	django-admin startproject mysite
## 启动django服务器
	python manage.py runserver 127.0.0.1：8000

## 创建APP
	python manage.py startapp article
## 注册APP（settings）
## 配置访问路径（urls）

## 对模型的更改创建新的迁移表
	python manage.py makemigrations
## 应用迁移到数据库中
	python manage.py migrate
	
## 创建管理员账号（Superuser）
	python manage.py createsuperuser
	Username: admin
	Email address: 1474423043@qq.com
	Password: 24186211tkz
	Password (again): 24186211tkz
	Superuser created successfully.
## 注册到后台中
	
## 改写视图函数	
	
## 安装Markdown
Markdown是一种轻量级的标记语言，它允许人们“使用易读易写的纯文本格式编写文档，然后转换成有效的或者HTML文档。
	https://help.coding.net/
	pip install markdown
## 代码高亮

在static目录中新建一个目录md_css/，一会儿放置代码高亮的样式文件。

重新打开一个命令行窗口，进入虚拟环境，安装Pygments：pip install Pygments

Pygments是一种通用语法高亮显示器，可以帮助我们自动生成美化代码块的样式文件。

在命令行中进入刚才新建的md_css目录中，输入Pygments指令：

	pygmentize -S monokai -f html -a .codehilite > monokai.css

这里有一点需要注意, 生成命令中的 -a 参数需要与真实页面中的 CSS Selector 相对应，即.codehilite这个字段在有些版本中应写为.highlight。如果后面的代码高亮无效，很可能是这里出了问题。

回车后检查一下，在md_css目录中是否自动生成了一个叫monokai.css的文件，这是一个深色背景的高亮样式文件。

## 增加弹窗
	Layer弹窗组件。https://layer.layui.com/

## 用户管理
	python manage.py startapp userprofile

@login_required是一个Python装饰器。
装饰器可以在不改变某个函数内容的前提下，给这个函数添加一些功能。
具体来说就是@login_required要求调用user_delete()函数时，用户必须登录；
如果未登录则不执行函数，将页面重定向到/userprofile/login/地址去。
https://docs.djangoproject.com/en/2.1/topics/auth/default/#django.contrib.auth.decorators.login_required

## 重置密码
Django 的验证系统
https://docs.djangoproject.com/zh-hans/2.1/topics/auth/default/

Django-password-reset的第三方库。
	pip install -U django-password-reset
	
第三方库也是app，需要在/my_blog/settings.py中注册：


阅读官方文档，尝试去改写模板文件，让页面更加匹配自己网站的风格。
官方文档在这里：https://django-password-reset.readthedocs.io/en/latest/index.html
GitHub：django-password-reset


## 邮箱的相关配置
在/my_blog/settings.py末尾添加发送邮箱的相关配置

	# SMTP服务器，改为你的邮箱的smtp!
	EMAIL_HOST = 'smtp.qq.com'
	# 改为你自己的邮箱名！
	EMAIL_HOST_USER = 'your_email_account@xxx.com'
	# 你的邮箱密码
	EMAIL_HOST_PASSWORD = 'your_password'
	# 发送邮件的端口
	EMAIL_PORT = 25
	# 是否使用 TLS
	EMAIL_USE_TLS = True
	# 默认的发件人
	DEFAULT_FROM_EMAIL = 'xxx的博客 <your_email_account@xxx.com>'


## 用户头像字段 
由于avatar字段为图像字段，需要安装第三方库Pillow来支持：
	pip install Pillow

## 分页
利用轮子
写一个完善的分页功能是有些难度的，
Django已经帮你准备好一个现成的分页模块了
（Django把大部分基础功能都替你准备好了！）。
内置模块虽然简单，但是对博客来说完全足够了。
我们要用到的是Paginator类。
官网
https://docs.djangoproject.com/zh-hans/2.1/topics/pagination/

## Q对象。
如果想对多个参数进行查询怎么办？比如同时查询文章标题和正文内容。这时候就需要Q对象。

更加复杂、深度定制的搜索可以借助第三方模块，如Haystack。


## markdown.markdown()和markdown.Markdown()的区别
https://python-markdown.github.io/extensions/toc/


## 类视图
https://docs.djangoproject.com/zh-hans/2.1/ref/class-based-views/generic-editing/


## django-ckeditor富文本编辑器
	pip install django-ckeditor

## 矢量图标
https://fontawesome.com/

## Abouolia的粘性侧边栏插件



## 用django-notifications实现消息通知
	pip install django-notifications-hq
	python manage.py migrate
	注册app：
	在根路由中安装路径：
	path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
	接下来你就可以在项目的任何地方发送通知了！
	from notifications.signals import notify
	notify.send(actor, recipient, verb, target, action_object) 
	 
	actor：发送通知的对象
	recipient：接收通知的对象
	verb：动词短语
	target：链接到动作的对象（可选）
	action_object：执行通知的对象（可选) 
	有点绕，举个栗子：杜赛 (actor) 在 Django搭建个人博客 (target) 中对 你 (recipient) 发表了 (verb) 评论 (action_object)。 
	

## 第三方登录 
Django-allauth，它不仅包含一整套的本地注册、登录、管理的解决方案，
还支持GitHub、Twitter、微博、微信甚至百度等几十种第三方登录方式
	pip install django-allauth
	python manage.py migrate








	
	 
	 