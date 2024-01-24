# -*- encoding: utf-8 -*-
# File : 03模块.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/24 14:43

'''
    模块的作用： 快速实现功能的工具包 是一个py文件 里面有 类 函数 变量
    导入模块的语法
    [from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]
    常用组合形式
        - import 模块名
        - from 模块名 import 类、变量、方法等
        - from 模块名 import *
        - import 模块名 as 别名
        - from 模块名 import 功能名 as 别名
'''

# 使用time包使用sleep功能
# import time
from time import sleep
print('Hello')
# time.sleep(5)
sleep(5)
print('Hi!')

# from time import *
# sleep(5)

# 别名
from time import sleep as shuimian
shuimian(5)