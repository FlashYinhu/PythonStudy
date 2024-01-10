# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/9 18:20
# 在一个函数的里面调用另一个函数
num = 10
num2 = 11


def f1():
    print('11111111')


def f2():
    f1()
    print('22222222')
    print('33333333')
    # 局部变量相当于新定义的num 和全局变量num无任何关系
    num = 3
    # 设置内部定义的变量为全局变量
    global num2
    num2 = 3


f2()
print(num)
print(num2)

