# -*- encoding: utf-8 -*-
# File : 06字典-02的方法和特点.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/19 15:34

# 新增元素 语法 字典[Key] = Value 如果Key不存在则新增元素 如若Key存在则修改元素
my_dictionary = {'kangyinhu': 66, 'zhangrui': 77, 'xiaolei': 88}
print(f'初始字典为{my_dictionary}')

#新增元素
my_dictionary['zhangfei'] = 55
print(f'添加新元素后的字典为:{my_dictionary}\n')

# 修改元素
score_init = my_dictionary['kangyinhu']
print(f'修改前kangyinhu的分数为{score_init}')
my_dictionary['kangyinhu'] = 100
score_updated = my_dictionary['kangyinhu']
print(f'修改后kangyinhu的分数为{score_updated}\n')

# 删除元素 pop(Key)
print(f'删除元素前的字典为{my_dictionary}')
value = my_dictionary.pop('xiaolei')
print(f'删除键值对的值为{value},删除后的字典为{my_dictionary}\n')

# 清空元素
my_dictionary.clear()
print(f'字典被清空了,清空后的字典为{my_dictionary}\n')

# 获取全部Key 字典.keys
my_dictionary = {'liubei': 88, 'guanyu': 100, 'zhangfei': 66}
keys = my_dictionary.keys()
print(f'字典的内容为{my_dictionary}\n字典中的Key有{keys}\n类型是{type(keys)}\n')

# 遍历字典 不支持while
print('通过获取全部的key遍历字典')
for temp in keys:
    print(f'{temp}: {my_dictionary[temp]}')
print()
print('直接对字典进行for循环，每一次循环都是直接得到key')
for key in my_dictionary:
    print(f'{key}: {my_dictionary[key]}')
print()

# 统计字典内元素的数量
print(f'字典{my_dictionary}中的元素数量为{len(my_dictionary)}')
