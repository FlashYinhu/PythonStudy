# -*- encoding: utf-8 -*-
# File : 04-01自定义模块.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/24 14:59

from my_module import test as add       # 此时内置变量__name__ != '__main__'
add(1, 2)

# 注意 当不同模块中的方法重复时 后调用的方法会覆盖前调用的方法
# from my_module1 import my_test 
# from my_module2 import my_test
# mytest(1, 2) 此时会调用my_module 2 中的方法

# 如果一个文件中有'__all__'变量 当使用from xxx import * 导入时，只能导入这个列表中的元素
from my_module2 import *
test_A(2, 3)
test_B(2, 3)
# test_C(2, 3)              # 不在 __all__ = ['test_A', 'test_B'] 列表中