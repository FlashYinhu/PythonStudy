# -*- encoding: utf-8 -*-
# File : 05包.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/24 15:15

'''
    python的包是一个文件夹 包含了若干python模块 和 __init__.py的文件 缺一不可 没有的话就是文件夹
    导入包
        - 方法1 import 包名.模块名
            导入成功后通过 包名.模块名.目标进行使用
'''
import my_package.module1
import my_package.module2
import my_package.module3

my_package.module1.info_print1()
my_package.module2.info_print2()
my_package.module3.info_print3()

print('from导入模块')
from my_package import module1
module1.info_print1()

print('从包中模块直接导入方法')
from my_package.module2 import info_print2
info_print2()

# 和模块中的__all__含有的方法一样 
# 包中的__init__.py 中也有__all__变量 用于管理 import *