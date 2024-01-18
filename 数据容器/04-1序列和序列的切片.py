# -*- encoding: utf-8 -*-
# File : 04序列和序列的切片.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/18 20:26

"""
    什么是序列 和 序列的切片操作
    序列指的是内容连续、有序、可以使用下表索引的一类数据容器
    序列支持切片：列表、元组、字符串均支持切片操作
    切片 从一个序列中取出一个子序列
    语法：序列[起始下标:结束下标:步长]
        - 起始下标为空视作从头开始
        - 结束下标为空视作取到结尾
            - 步长为1表示一个个取元素
            - 步长为2表示每次跳过1个取元素
            - 步长为N表示每次跳过 N - 1个取元素
            - 步长为负数表示反向取 同时注意开始和结束也要反向标记
"""

# 对list进行切片 从1开始，到4结束，步长1
mylist = ['kangyinhu', 'xiaolei', 'zhangrui', 'caixukun', 'zhangfei', 'lvbu', 'weiyixiao', 'weixiaobao']
new_list = mylist[1: 4 : 1]

# 对tuple进行切片
mytuple = ('zhangsanfeng', 'yangguo', 'guojing', ' xiaolongnv', 'liubei', 'guanyu', 'zhangfei', 'caocao')
new_tuple = mytuple[ : : 1]

# 对str进行切片
mystr = 'kangyinhushiyigedashuaigezhangruishiyigedameinv'
new_mystr  = mystr[ : : 2]

# 对列表进行切片
mylist2 = (0, 1, 2 , 3, 4, 5, 6, 7, 8, 9, 10)
new_mylist2 = mylist2[3: 1: -1]

# 对元组进行切片
mytuple2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
num = len(mytuple2)
new_mytuple2 = mytuple2[ : :-2]

print(new_list)
print(new_tuple)
print(new_mystr)
print(new_mylist2)
print(new_mytuple2)