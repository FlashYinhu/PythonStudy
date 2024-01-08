#  Python自动化脚本

> 简洁高效 应用丰富 上层API 简单高效 底层C/C++稳定高效 人生苦短 我用python
>
> 本机python环境(默认) C:\Users\Yinhu\AppData\Local\Programs\Python\Python312

## Linux安装python

~~~shell
yum install wget zlib-devel bzip2-decel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make zlib zlib-devel libffi-devel -y
wget https://www.python.org/ftp/python/3.12.1/Python-3.12.1.tgz
tar -xvf Python-3.12.1.tgz
cd Python-3.12.1
./configure --prefix=/usr/local/python3.12.1
make %% make install
~~~

配置软连接再任意位置 `/usr/bin/python`即可进入python解释器环境

~~~shell
rm -f /usr/bin/python
ln -s /usr/local/python3.12.1/bin/python3.12.1 /usr/bin/python
~~~

修改yum相关依赖,因为linux中yum本质上依赖python2.0环境

~~~shell
vim /usr/libexec/urlgrabber-ext-down 
#第一行 /usr/bin/python 改为 /usr/bin/python2
vim /usr/bin/yum
#第一行 /usr/bin/python 改为 /usr/bin/python2
~~~

至此直接运行 `python`也可以进入解释器环境

## 基础

cmd中执行python文件 `python 文件路径`,集成开发工具 IDE: PyCharm,`ctrl + d`复制一行代码

标识符命名规则

## 高阶加强



## 大数据分析PySpark