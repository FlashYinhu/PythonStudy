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

# 元组的嵌套
t6 = ('kangyinhu', ('xiaolei', 'zzz'))
print(f't6的内容是{t6}, 类型是{type(t6)}')

# 通过下标索引取出内容
t7 = (('kangyinhu', 'xiaolei'), 'zhangrui')
print(f'从嵌套元组中取值:{t7[0][0]}')

# 元组的方法，因为元组不可修改 所以方法相对少一点
t8 = ('niudun', 'aiyisitan', 'jialilve', 'dikaer', 'kawendixu', 'aiyisitan')
print(t8.index('kawendixu'))
print(t8.count('aiyisitan'))
print(len(t8))

# 元组的遍历
t9 = ('lvbu', 'zhangfei', 'zhugeliang', 'liubei', 'caocao', 'guanyu')
for element in t9:
    print(element, '', end='')
print()
index = 0
while index < len(t9):
    print(t9[index], '', end='')
    index += 1
print()

# 元组的注意事项
# t9[0] = 'liubei'
# TypeError: 'tuple' object does not support item assignment
# 元组中嵌套列表是可以修改的
t10 = (1, 2, [3, 4, 5], 6)
print(f't10的内容是:{t10}')
t10[2].append(1)
t10[2].extend([2, 3, 4, 5, 6])
print(f'修改t10中list之后的t10是:{t10}')

for temp in t10:
    if type(temp) is list:
        print(temp)
