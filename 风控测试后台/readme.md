# 风控测试平台readme
# 风控测试平台

## 重要

django框架下数据库不可混用，故开发时数据库要替换成本地数据库。
imac上使用数据库django4为生产库。



## 开发

### 创建虚拟环境

```
pipenv --python 2.7
pipenv shell

pip install -r requirements.txt 


```
pythonclient安装异常
```
xcode-select --install
export PATH="/usr/local/bin/:$PATH"
source .bash_profile 
```


```
# 导出依赖包
pip freeze > requirements.txt
```



###  初始化数据库



```
python manage.py makemigrations snippets
python manage.py migrate
```



### 启动服务

```
python manage.py runserver
```




## 部署

### uwsgi安装

```
nohup uwsgi --ini uwsgi.ini &
```
uwsgi.ini
```
[uwsgi]
#socket 为上线使用，http为直接作为服务器使用。
socket = 127.0.0.1:8000#ip和端口号可以改
http = 127.0.0.1:8001
#项目目录
chdir=/Users/test/RiskControl/tutorial
module=tutorial.wsgi:application
#虚拟环境目录
home = /Users/test/RiskControl/tutorial/venv
master = true         
processes=4
threads=2
```




## mysql搭建
Docker

```
docker rm mysqllocal

docker run -p 3307:3306 --name mysqllocal -v ~/docker/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456  -d mysql

docker start mysqllocal


```

brew安装

```
brew install mysql
```





### 初始化密码

```

use mysql;
update user set host = '%' where user = 'root';
mysqladmin -u root password
mysql -u root
mysql -h localhost -u root -p -P 3306


```


### 导出数据库数据
未避免数据库结构与django migration记录不匹配，执行`python manage.py migrate`后，导出数据库备份。

```
mysqldump  -hlocalhost -p123456  -uroot --databases django4 > ./django4-`date "+%Y-%m-%d-%H:%M:%S"`.sql
```