# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/10 21:00
"""
    元组tuple一旦定义完成，就不可进行修改（只读的列表）
"""

# 定义一个元组
t1 = (1, "Hello", True)
t2 = ()
t3 = tuple()
print(f't1的内容是{t1}, 类型是{type(t1)}')
print(f't2的内容是{t2}, 类型是{type(t2)}')
print(f't3的内容是{t3}, 类型是{type(t3)}')
# 定义单个元素的元组
t4 = ('kangyinhu')
print(f't4的内容是{t4}, 类型是{type(t4)}')
t5 = ('kangyinhu', )
print(f't5的内容是{t5}, 类型是{type(t5)}')
t6 = ('kangyinhu', ('xiaolei', 'zzz'))
print(f't6的内容是{t6}, 类型是{type(t6)}')

print("kangyinhu")
