# -*- encoding: utf-8 -*-
# File : my_module.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/24 14:58

"""
    这是一个自定义模块
"""

def test(a, b):
    print(a + b)

# __main__变量 当且仅当只执行该文件时调用
# 防止其他文件调用本文件时执行测试方法
if __name__ == '__main__':
    test(1, 2)