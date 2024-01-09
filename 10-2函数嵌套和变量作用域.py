# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/9 18:20
# 在一个函数的里面调用另一个函数

def f1():
    print('11111111')


def f2():
    f1()
    print('22222222')
    print('33333333')


# 调用
f2()

