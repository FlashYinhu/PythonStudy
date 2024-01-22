# -*- encoding: utf-8 -*-
# File : 03-02lambda匿名函数.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/22 17:25

"""
    def关键字可以定义带有名称的关键字 lambda关键字可以定义匿名函数(无名称)
    有名称的函数可以基于名称重复使用 没有名字的函数只可以临时使用一次
    语法 lambda 传入参数:函数体(只能写一行代码)
"""

def my_function(f1):
    result = f1(1, 2)
    print(result)

my_function(lambda num1, num2 : num1 + num2)