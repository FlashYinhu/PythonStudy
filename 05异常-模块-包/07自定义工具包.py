# -*- encoding: utf-8 -*-
# File : 07自定义工具包.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/24 16:13

"""
    利用自定义工具包 实现
        - 字符串逆序
        - 字符串截取
        - 文件内容显示
        - 文件内容追加

    测试用例
        'nihaowodemingzijiaokangyinhu'
        'kangyinhu' 4 7
        ./test.txt
        ./test.txt 'This is my first try in using my_utils'
"""

import my_utils.str_util
from my_utils.file_util import print_file_info
from my_utils.file_util import append_to_file
mystr = 'nihaowodemingzijiaokangyinhu'
namestr = 'kangyinhu'
yin_l = 4
yin_r = 7

print(f'字符串{mystr}的逆序结果是{my_utils.str_util.str_reverse(mystr)}')
my_utils.str_util.substr(namestr, yin_l, yin_r)
print_file_info('./test.txt')
append_to_file('./test.txt', '这是第1次调试')