# -*- encoding: utf-8 -*-
# File : 06字典.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/19 01:56
"""
    Python中的字典和生活中的字典十分相似
        生活中的字典通过 字 找出对应的 含义
        Python中的字典通过 key 找出对应的 value
    
    字典的定义同使用{},但是存储的元素是一个一个的"键值对"
"""

# 定义字典
my_dictionary = {"kangyinhu" : 100 ,"zhangrui" : 99 ,"xiaolei" : 98 }

# 定义空的字典, 空集合的定义只有 set_empty = set(), 因为 {}被空字典使用
my_dictionary_empty1 = {}
my_dictionary_empty2 = dict()
print(f'空字典1的内容是{my_dictionary_empty1},类型是{type(my_dictionary_empty1)}')
print(f'空字典2的内容是{my_dictionary_empty2},类型是{type(my_dictionary_empty2)}')

# 字典中的Key也不可以重复 重复定义时新的会把老的直接覆盖掉
my_dictionary2 = {'kangyinhu' : 100, 'kangyinhu' : 99}
print(f'重复定义key的字典的内容是:{my_dictionary2}')

# 通过字典中的Key获取Value
score = my_dictionary['kangyinhu']
print(f'kangyinhu的分数为{score}\n')

# 定义嵌套字典: 字典的key和value可以是任意数据类型(key不可以为字典)
my_dictionary_nested = {
    'kangyinhu': {
        'yuwen': 77,
        'shuxue': 88,
        'yingyu' : 99
    },
    'zhangrui': {
        'yuwen': 88,
        'shuxue': 99,
        'yingyu': 100
    },
    'xiaolei': {
        'yuwen': 66,
        'shuxue': 77,
        'yingyu': 88
    }
}

# 从嵌套字典中获取数据
score1 = my_dictionary_nested['kangyinhu']['yingyu']
print(f'kangyinhu的yingyu成绩为{score1}')