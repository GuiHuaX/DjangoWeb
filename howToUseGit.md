## 如何使用`git`

*	进入项目根目录
### 初始化一个git本地仓库
*	使用命令`git init`
*	此时会在本地创建一个 .git 的文件夹
### 添加远程仓库
*	使用`git remote add origin https://gitee.com/你的码云用户名/XXXX` 
### 将码云上的仓库pull到本地文件夹
*	使用`git pull origin master`命令
*	期间需要输入gitee上面的账号和密码。
### 将要上传的文件，添加到刚刚创建的文件夹  
*	使用`git add .`  注意：（. 表示所有的）
*	或者`git add + 文件名`           
*	目的是将文件保存到缓存区 
### 添加文件描述
*	使用`git commit -m '新添加的文件内容描述'`
### 将本地仓库推送到远程仓库
*	使用`git push origin master -f`
*	执行`git push`之后，在gitee中就能看到推送上去的项目了


