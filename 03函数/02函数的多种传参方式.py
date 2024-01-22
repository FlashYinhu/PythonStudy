# -*- encoding: utf-8 -*-
# File : 02函数的多种传参方式.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/22 16:33
"""
    位置参数、关键字参数、不定长参数、缺省参数
"""
# 位置参数
def user_info(name, age, gender):
    print(f'Your name is{name}, age is {age}, gender is {gender}')

user_info('kangyinhu', 24, '男')

# 关键字参数 键 = 值 位置可以不固定 也可以和位置参数混用但是位置参数必须在前面
def emp_info(id, salary, level):
    print(f'The staff\'s id is {id}, salary is{salary}, level is {level}')
emp_info(salary= 20000, level= 5, id= '123412412415')

# 缺省参数/默认参数 用于函数定义 为参数提供默认值 必须定义在最后
# 调用函数时可以不传默认参数的值
# 注意 位置参数必须出现在默认参数的前面 包括函数定义和调用
def student_info(name, age, score, class_num, school = 'NNU'):
    print(f'Your name is {name}, age is {age}, score = {score}, class num = {class_num}, school is {school}')
student_info('kangyinhu', 24, 100, 1703)

"""
    不定长参数 ： 位置传递的不定长和关键字传递的不定长
    位置传递的不定长 传入的所有参数都会被 args 收集变量并且根据传入参数的位置合并为一个元组tuple， args存储为元组类型
"""

# 位置不定长 参数 : *args
def teacher_info(*args):
    print(f'The args received are{args}, type is {type(args)}')
teacher_info('liujingbo', 40, 'Rugao High School', 'women', False)

# 关键字不定长 参数 **kwargs    // keyword  存储为字典
def car_inof(**kwargs):
    print(f'The kwargs received are {kwargs}, type is {type(kwargs)}')
car_inof(brand = 'BMW', factory = 'biyadi', made_in = 'CHN', id = '312512412')