# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/10 14:26
"""
    python中的数据容器，一种可以容纳多份数据的数据类型
    容纳的每一份数据称之为一个元素，每一个元素可以是任意类型的数据
    例如字符串，数字，布尔类型等。

    列表 元组 字符串 集合 字典
    list tuple str set dict
    各有特点，但都满足容纳多个容器
"""
name_list = ['kangyinhu', 'zhangrui', 'xiaolei']
print(name_list)
print(type(name_list))

# 列表中的元素类型不受限制
my_list = ['kangyinhu', 666, True]
print(my_list)
print(type(my_list))

# 可以在列表中再存入列表
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list1)
print(type(list1))

# 列表的下标 list index
list2 = [3, 2, 0, 6, 8, 2]
print('===按下标打印===')
for i in range(6):
    print(i, list2[i])
print('===逆序打印===')
# -1 就是倒数第一个，-2就是倒数第二个，以此类推
for i in range(1, 7):
    print(-i, list2[-i])

# 嵌套列表取值 4
print('取出嵌套列表中的值:4')
list3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"list3中第二个元素的第一个元素是:{list3[1][0]}")

# 字符串逆序
name = 'kangyinhu'
print(name)
for i in range(len(name)):
    j = -i - 1
    print(name[j], end='')
