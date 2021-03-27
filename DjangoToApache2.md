## 部署`Django`项目在`Apache2`服务器上

#### 环境搭建
    安装python：sudo apt-get install python3.7
    安装Django：pip3 install Django`
    安装Apache：sudo apt-get install apache2
#### 给你的`Apache2`安装`Python`解释器。
    sudo apt-get install libapache2-mod-wsgi      #Python2
    sudo apt-get install libapache2-mod-wsgi-py3  #Python3
#### 修改`Apache2`配置文件
    sudo vi /etc/apache2/sites-available/mysite.conf 
这里边包含了你所有的网站配置信息，包括Apache如何查找静态文件(js/css/images)，网站上传的文件存在哪里，最重要的，包含了Apache识别Django的wsgi文件。
    
    #<VirtualHost *:80>
    ServerName www.yourdomain.com
    #ServerAlias otherdomain.com
    #ServerAdmin youremail@gmail.com
    
    # 存放用户上传图片等文件的位置，注意去掉#号
    #Alias /media/ /var/www/ProjectName/media/ 
                
    # 静态文件(js/css/images)的存放位置
    Alias /static/ /var/www/ProjectName/static/                
    
    # 允许通过网络获取static的内容
    <Directory /var/www/ProjectName/static/>                  
        Require all granted
    </Directory>
    
    # 最重要的！通过wsgi.py让Apache识别这是一个Django工程，别漏掉前边的 /
    WSGIScriptAlias / /var/www/ProjectName/ProjectName/wsgi.py     
    # wsgi.py文件的父级目录，第一个ProjectName为Django工程目录，第二个ProjectName为Django自建的与工程同名的目录
    <Directory /var/www/ProjectName/ProjectName/>                  
    <Files wsgi.py>
        Require all granted
    </Files>
    </Directory>
    
    </VirtualHost>

通过修改上面的文件，你就可以让Apache找到你的Django工程，上边可以修改的内容包括：
    80：修改80为其他数字，可以更改你的端口号，国内的电信貌似把80端口给封了（如果你的域名没有备案的话）。注意，还要修改/etc/apache2/port.conf文件中的Listen *port*。
    ServerName：后边改成你自己的域名，如果没有的话就用IP代替。注意，如果改成了域名，还需要修改Django工程下的seeting.py文件，将其ALLOWED_HOSTS=[]改为ALLOWED_HOSTS=['www.yourdomain.com']，多个域名可以通过逗号隔开。
    ServerAlias：你的其他域名或IP。

#### 配置文件生效
    sudo a2ensite yoursite.conf
#### 配置文件失效
    sudo a2dissite yoursite.conf

#### 重启`Apache2`
    sudo service apache2 restart
#### 修改`Django`的`wsgi.py`文件
修改上面说的`mysite/mysite/wsgi.py`为如下格式

    import os
    from os.path import join,dirname,abspath
    PROJECT_DIR = dirname(dirname(abspath(__file__)))

    import sys
    sys.path.insert(0,PROJECT_DIR)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "examsys.settings")

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

这个配置文件的作用是让Apache找到Djanog.
每次你修改Django工程文件之后，都最好restart一下，让它生效。