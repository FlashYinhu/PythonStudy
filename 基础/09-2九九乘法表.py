# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/8 20:36

# print 不换行的方法
print("hello", end='')
print("pyt hon", end='')
print('')
# 制表符的应用
print("kang\tyin \thu")
print("zhang\trui")

"""
    九九乘法表，分析
    1. 控制行的循环 (i<=9)
    1. 控制每一行输出的循环(j<=i)
"""
print('使用while循环实现99乘法表')
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}\t", end='')
        j += 1
    i += 1
    # print输出空内容就是输出一个换行
    print()

print()
print('使用for循环实现99乘法表')
for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print(f"{j}*{i}={j*i}\t", end='')
    print()

print()
print('另一种方法')
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}*{i}={j * i}\t", end='')
    print()