# -*- encoding: utf-8 -*-
# File : 05集合.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/19 01:12
"""
    集合的定义格式、特点和常见操作
        列表可修改，支持重复元素且有序
        元组字符串不可修改，支持重复元素且有序
        局限性在于支持重复元素，如果需要对数据进行去重处理，元组和列表就不方便了
        集合最主要的特点就是：不重复且无序
        语法：集合变量名 = {元素1 ,元素2 ,元素3 , ....}
             定义空集合 变量名 = set()
"""

# 集合的定义
name_set = {'kangyinhu', 'zhangrui', 'xiaolei'}
name_set_empty = set()
print(f'name_set的内容是:{name_set},\n类型是{type(name_set)}')
print(f'name_set_empty的内容是:{name_set_empty},\n类型是{type(name_set_empty)}\n')

# 集合是无序的，不支持下表索引访问，集合和列表一样允许修改
# 集合的修改方法
# 添加新元素
print(f'name_set的内容是:{name_set}')
name_set.add('zhangfei')
print(f'name_set添加不同元素后的结果是{name_set}')
name_set.add('kangyinhu')
print(f'name_set添加相同元素后的结果是{name_set}')
name_set.remove('zhangfei')
print(f'name_set移除元素后的结果是{name_set}')
element = name_set.pop()
print(f'集合被随机取出的元素是{element},取出元素后的集合为{name_set}\n')

# 清空集合
print(f'name_set的内容是:{name_set}')
name_set.clear()
print(f'清空后的集合为{name_set}\n')

# 取两个集合的差集
name1 = {'liubei', 'guanyu', 'zhangfei'}
name2 = {'liubei', 'caocao', 'sunquan'}
name_different = name1.difference(name2) # 集合1有的而集合2没有的 集合1和2内容不变
print(f'name1中的元素为{name1}\nname2中的元素为{name2}\nname1和name2的差集为{name_different}\n')

# 消除2个集合的茶几
# 语法：集合1.difference_update(集合2)
# 功能对比集合1和集合2，在集合1内删除和集合2相同的元素
# 结果 集合1被修改，集合2不变
print(f'集合1中的元素为{name1}\n集合2中的元素为{name2}')
name1.difference_update(name2)
print(f'从集合1中删除和集合2中重复的元素后集合1为{name1}\n此时name2的内容仍然为{name2}\n')

# 两个集合合并为一个 得到新的集合，集合1和集合2的内容不变
set1 = {1, 2 ,3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(f'set1中的内容为{set1}\nset2中的内容为{set2}\n两个集合合并后新的集合为{set3}\n')

# 统计集合的元素数量
set_num = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0}
num = len(set_num)
print(f'数字集合的内容为{set_num},共计{num}个元素')

# 集合的遍历
for temp in set_num:
    print(temp, end='')