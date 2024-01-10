# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/8 17:11
"""
    python中的数据结构有 数字 字符串 列表 元组 集合 字典
    比较运算符有 ==, !=, >, <, >=, <= 6种
"""
# bool数据类型的演示
bool1 = True
bool2 = False
print(f"bool1的内容是: {bool1},类型是：{type(bool1)}")
print(f"bool1的内容是: {bool2},类型是：{type(bool2)}")
# 比较运算符的演示
num1 = 10
num2 = 10
num3 = 15
name1 = "kangyinhu"
name2 = "zhangrui"
print(f"10 == 10的结果是: {num1 == num2}")
print(f"10 != 15的结果是: {num1 != num3}")
print(f"name1 == name2的结果是: {name1 == name2}")
print(f"10 < 15的结果是: {num1 < num3}")
print(f"15 > 10的结果是: {num3 > num2}")
print(f"15 >= 10的结果是: {num3 >= num2}")
print(f"10 <= 15的结果是: {num1 <= num2}")

result = 10 > 5
print(result, type(result))

