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
# 语法 字符串.replace(字符串1, 字符串2)
# 将字符串内的全部字符串1 替换为字符串2
# 注意并不是修改字符串本身 而是得到一个新的字符串
print('将字符串中的\'yin\'替换为YIN')
new_name = name.replace('yin', 'YIN')
print(f'原来的字符串是: {name}\n替换后的字符串为:{new_name}\n替换后的字符串是新的字符串\n')

# 字符串的分割
# 语法： 字符串.split(分割字符串)
# 按照指定的分隔符字符串将字符串划分为多个字符串并存入列表对象中
str1 = 'abcdeAfghijkAlmnopqArstuvwAxyz'
list1 = str1.split('A')
print(f'原来的字符串为{str1},\n按照\'A\'分割后得到的新的对象为{list1}')
print(f'被分割的字符串仍然是{str1}')

# 字符串的规整操作
# 删除前后空格 语法：字符串.strip()
# 去除前后指定字符串 语法：字符串.strip(字符串)
str2 = '  kangyinhu  '
new_str2 = str2.strip()
print(f'规整前的字符串为"{str2}"\n规整后的字符串为"{new_str2}"')
str3 = '123kangyinhu321'
new_str3 = str3.strip('312')
print(f'规整前的字符串为"{str3}"\n规整后的字符串为"{new_str3}"')

# 统计字符串中某个字符串出现的次数
str4 = 'kangyinhuyinkangyinhukangyinhukangyinhu'
print(f'字符串{str4}中"kang"出现的次数为{str4.count('kang')}')

# 统计字符串的长度
str5 = 'kangyinhuaizhangrui'
print(f'字符串{str5}的长度是{len(str5)}')

print(len(name))
for i in range(len(name)):
    print(name[- i - 1], end='')
    i += 1

block = ['', '', '']

