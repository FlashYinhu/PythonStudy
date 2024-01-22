# -*- encoding: utf-8 -*-
# File : 03匿名函数.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/22 17:11

# 掌握函数作为传递参数 是一种计算逻辑的传递而非数据的传递 
# 任何逻辑都可以自定义并作为函数传入

# 定义一个函数 接受另一个函数作为传入参数
def my_function(add, sub, muti, div):
    print(f'{type(add)}')
    print(f'{type(sub)}')
    print(f'{type(muti)}')
    print(f'{type(div)}')
    number1, number2 = 125, 25
    print(f'{add(number1, number2)}, {sub(number1, number2)}, {muti(number1, number2)}, {div(number1, number2)}')

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def muti(x, y):
    return x * y

def div(x, y):
    return x / y

my_function(add, sub, muti, div)