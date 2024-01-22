# -*- encoding: utf-8 -*-
# File : 05-01文件操作综合案例.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/22 20:19

"""
    需求 有一份账单文件 记录了消费收入的具体记录 形如
    name, date, money, type, remarks 
    kangyinhu, 2022-09-17, 10000, 收入, 正式
    xiaolei, 2023-08-04, 8888, 消费, 正式
    kangyinhu, 2021-06-04, 6000, 收入, 测试
    kangyinhu, 2022-08-04, 12400, 收入, 正式
    liangjiahui, 2022-07-04, 56000, 消费, 测试
    kangyinhu, 2016-08-04, 30000, 收入, 正式
    kangyinhu, 2022-04-25, 10660, 收入, 正式
    zhangrui, 2015-08-04, 10000, 收入, 消费
    kangyinhu, 2012-08-25, 1040, 收入, 正式
    kangyinhu, 2022-08-04, 70000, 收入, 正式

    要求 读取文件 将文件写出到bill.txt.bak 
    同时将文件内标记为测试的数据行进行丢弃
"""

fr = open('./04文件/05-00bill.txt', 'r', encoding= 'UTF-8')
fw = open('./04文件/05-00bill.txt.bak', 'w', encoding= 'UTF-8')
for temp_line in fr:
    temp_line = temp_line.strip()
    # temp_list  = temp_line.split(',')
    # if temp_list[-1] == '测试':
    #     continue      
    if temp_line.split(',')[-1] == ' 测试':
        continue            # 略过测试内容
    fw.write(temp_line)
    fw.write('\n')

# close两个对象 写出文件close()会自动调用flush()
fr.close()
fw.close()