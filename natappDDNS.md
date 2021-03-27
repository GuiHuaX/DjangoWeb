
参考：https://natapp.cn/article/nohup


隧道：authtoken=3be3b485893d6960


》》》》》 以下为后台运行，即可以把当前终端窗口关闭，而不会影响隧道，还可查看隧道IP 《《《《《

	首先,要确保常规方式运行natapp 没有任何问题.

	我们将natapp放在 /usr/local/natapp/ 下

	cd /usr/local/natapp


	然后运行

	./natapp -authtoken=3be3b485893d6960


	正常运行如下

	浏览器访问等测试,均无任何问题.

	这是,如果关掉窗口,就是关掉了natapp程序,所以会掉线.

	下面利用 nohup 实现natapp(ngrok)后台运行方法

	很简单,运行

	nohup ./natapp -log=stdout &
	注意一定要加上 -log=stdout


	此时,按Ctrl+C 退出,或者直接关闭窗口都可以.


	另开一个窗口检查一下

	ps -ef|grep natapp


	可以看到natapp进程代表运行成功!如果运行了多次,则会出现多个natapp进程,需要结束进程.下面 那个 2790的,代表查找程序本身,忽略掉.



	找到natapp进程的pid 2777 ,如果要结束进程,运行

	kill -9 2777


	nohup 默认会在当前目录 创建 nohup.out 文件,会记录natapp运行日志,为避免日志过大,可以将日志等级降低 如

	nohup ./natapp -log=stdout -loglevel=ERROR &
	nohup ./natapp -log=stdout -loglevel=INFO &
	
	ps ef | grep natapp
	保留两个natapp线程，
	一个是./natapp -log=stdout -loglevel=ERROR &
	另一个是./natapp -log=stdout -loglevel=INFO &
	
	cat nohub.out

	如果需要开机自启动,请参考 以下 开机自启动 方法：
	
	

》》》》》》》以下为开机自启动，个人觉得不是很好用，暂时不能查看隧道IP《《《《《《《

	## 运行natapp客户端
	1. 在 https://natapp.cn 官网 下载客户端.
	放在`/usr/local/natapp/`目录下

	运行
	```
	sudo chmod a+x /usr/local/natapp/natapp
	```
	给予可执行权限
	 
	2.下载`config.ini`放置在同级目录,config 配置说明请见 https://natapp.cn/article/config_ini

	将authtoken=3be3b485893d6960 等配置 写入 config.ini中.

	需要注意的是 务必关闭 关闭Web管理界面 (登录网站->我的隧道->配置)

	3.测试运行情况
	```
	./usr/local/natapp/natapp
	```
	实际测试穿透应用,确保无误,后关闭客户端

	##自启动脚本
	4.将启动脚本 ([下载](https://raw.githubusercontent.com/natapp/natapp_autostart/master/RaspberryPi/natapp)) 放在 `/etc/init.d/` 下

	给予 755权限
	```
	sudo chmod 755 /etc/init.d/natapp
	```

	5.测试 init.d 启动
	运行
	```
	sudo /etc/init.d/natapp start
	```
	
	查看natapp线程，把多余的 kill 掉
	```
	ps ef | grep natapp
	```
	
	同3,确保穿透应用运行无误.

	6.加入开机自启动
	```
	cd /etc/init.d
	sudo update-rc.d natapp defaults 90
	```
	此步骤需保证无任何错误输出

自启脚本：https://raw.githubusercontent.com/natapp/natapp_autostart/master/RaspberryPi/natapp

#!/bin/sh -e
### BEGIN INIT INFO
# Provides:          natapp.cn
# Required-Start:    $network $remote_fs $local_fs
# Required-Stop:     $network $remote_fs $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: autostartup of natapp for RaspberryPi
### END INIT INFO


NAME=natapp
DAEMON=/usr/local/natapp/$NAME
PIDFILE=/var/run/$NAME.pid

[ -x "$DAEMON" ] || exit 0

case "$1" in
  start)
      if [ -f $PIDFILE ]; then
        echo -n "$NAME already running"
        echo "."
    else
        echo "Starting $NAME..."
	    start-stop-daemon -S -x $DAEMON -p $PIDFILE -m -b -o -q || return 2
        echo "."
    fi
    ;;
  stop)
            echo "Stoping $NAME..."
        start-stop-daemon -K -p $PIDFILE -s TERM -o -q || return 2
        rm -rf $PIDFILE
        echo "."
    ;;
  restart)
    $0 stop && sleep 2 && $0 start
    ;;
  *)
    echo "Usage: $0 {start|stop|restart}"
    exit 1
    ;;
esac
exit 0




