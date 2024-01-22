# -*- encoding: utf-8 -*-
# File : 03-01文件的写入操作.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/22 19:59
import time


"""
    直接调用write() 不会真正地写入文件 而是会积攒在程序的内存中
    称之为缓冲区 当调用 flush()方法的时候才会真正写入文件中
    这样做的目的是防止频繁地操作硬盘导致效率下降(攒一堆 一次性写硬盘)
"""

# 打开文件 不存在文件时 w 会创建文件
f = open('./04文件/03-00.txt', 'w', encoding= 'UTF-8')
f.write("Hello! My name is kangyinhu! Nice to see you!")
f.flush()                       # 将内存中积攒的内容写入到硬盘的文件中
f.close()                       # close()方法是内置了flash功能

# 文件已经存在时 会将文件内容清空后写入
f = open('./04文件/03-00.txt', 'w', encoding= 'UTF-8')
intro = 'Hello! My name is kangyinhu! Nice to see you!'
for i in range(len(intro)):
    f.write(intro[- i - 1])
f.close()