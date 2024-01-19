# -*- encoding: utf-8 -*-
# File : 06字典-03综合应用.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/19 15:56

emp_dictionary = {
    'kangyinhu': {
        'department': 'test',
        'salary': 5000,
        'level': 1 
    },
    'zhangrui': {
        'department': 'product',
        'salary': 6000,
        'level' : 2
    },
    'xiaolei': {
        'department': 'develop',
        'salary': 10000,
        'level': 1
    },
    'liudehua': {
        'department': 'boss',
        'salary': 88888,
        'level': 99
    }
}

print(f'全体人员信息如下:')
for key in emp_dictionary:
    print(f'{key}: {emp_dictionary[key]}')

print()
for key in emp_dictionary:
    if emp_dictionary[key]['level'] == 1:
        emp_dictionary[key]['level'] += 1
        emp_dictionary[key]['salary'] += 1000
print(f'全体员工中级别为1的员工完成升职加薪操作, 更新后的信息为:')
for key in emp_dictionary:
    print(f'{key}: {emp_dictionary[key]}')