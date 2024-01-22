# -*- encoding: utf-8 -*-
# File : 04-01文件的追加操作.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/22 20:14

"""
    a模式追加 文件不存在会创建文件 文件存在会在最后追加写入文件
"""
f = open('./04文件/04-00.txt', 'a', encoding= 'UTF-8')
for i in range(100):
    f.write(f'{i} ')
f.flush()
f.close()