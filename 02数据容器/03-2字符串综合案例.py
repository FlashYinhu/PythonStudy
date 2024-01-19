# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/18 18:05

"""
    给定一个字符串'xxxxxxxxxx'
    1.统计字符串内有多少个'kang'
    2.将字符串内的空格全部替换为'|'
    3.按照'|'对字符串进行分割，得到新的列表
"""

str1 = 'kangyinhu kangyinhu kangyinhu kangyinhu kangyinhu kangyinhu kangyinhu'
count = str1.count('kang')
new_str1 = str1.replace(' ','|')
list1 = str1.split('|')
print(f'给定的字符串为{str1}\n其中"kang"的数量为{count}\n将字符串中的空格替换为管道符后的字符串为{new_str1}\n按管道符分割后得到的结果为{list1}')