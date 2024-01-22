# -*- encoding: utf-8 -*-
# File : 01函数的多返回值.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/19 17:17
def count_numbers():
    for i in range(1, 6):
        print(i)
    # 通过逗号分隔 返回多个返回值
    return 1, 'hello', False

x, y, z = count_numbers()
print(f'接受到的返回值为{x}, {y}, {z}')