# -*- encoding: utf-8 -*-
# File : 07数据容器的通用功能.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/19 16:38

my_list = [1, 2, 3, 4, 5]
my_tuple = (5, 6, 7, 8, 9)
my_str = 'kangyinhu'
my_set = {'a', 'e', 'i', 'o', 'u'}
my_dictionary = {'key_a': 1, 'key_b': 2, 'key_c': 3, 'key_d': 4, 'key_e': 5}

# 最大最小元素
print(f'字符串中最大的元素是{max(my_str)}')
print(f'字符串中最小的元素是{min(my_str)}\n')

# 容器转列表
print(f'字符串转列表的结果是:{list(my_str)}')
print(f'集合转列表的结果是:{list(my_set)}') # 取每个元素
print(f'字典转列表的结果是:{list(my_dictionary)}') # 抛弃Value取Key

# 容器转元组
print(f'字典转元组的结果是:{tuple(my_set)}\n')

# 容器转字符串
print(f'列表转的结果是{str(my_list)}')
print(f'元组转的结果是{str(my_tuple)}')
print(f'字符串转的结果是{str(my_str)}')
print(f'集合转的结果是{str(my_set)}')
print(f'字典转的结果是{str(my_dictionary)}\n')

# 容器转集合
print(f'字典转集合的结果是{set(my_dictionary)}\n')

# 容器不能转字典，因为缺少键值对

# 通用排序功能 sort(容器,[reverse = True]) 默认 反 参数为 False
my_num = [1, 0, 4, 8, 7, 3, 5, 2, 9, 6]
print(f'列表对象的正排序结果:{sorted(my_num)}') 
print(f'列表对象的逆排序结果是:{sorted(my_num, reverse= True)}\n')
# 注意 排序之后的结果均存储为列表对象！
print(f'字符串排序的结果是:{sorted(my_str)}')
print(f'集合排序的结果是:{sorted(my_set)}')
print(f'字典排序的结果是:{sorted(my_dictionary)}')