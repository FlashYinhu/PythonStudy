# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/14 14:53
"""
    数据容器中的字符串
    字符串是字符的容器 一个字符串可以存放任意数量的字符
"""

name = 'kangyinhu'
print(name)
# 通过下标索引取值
print(f'字符串中第五个字符是: {name[4]}')
print(f'字符串中倒数第五个字符是: {name[-5]}')

# 字符串同样是一个无法修改的数据容器
# name[1] = 'z'
# TypeError: 'str' object does not support item assignment
# del name[0]
# TypeError: 'str' object doesn't support item deletion
# name.remove()
# AttributeError: 'str' object has no attribute 'remove'
# name.pop('a')
# AttributeError: 'str' object has no attribute 'pop'
# name.append('zhangrui')
# AttributeError: 'str' object has no attribute 'append'

# index 方法
value = name.index('yin')
print(f'在字符串中查找\'yin\', 其起始下标是{value}')

# replace 方法


print(len(name))
for i in range(len(name)):
    print(name[- i - 1], end='')
    i += 1

block = ['', '', '']


