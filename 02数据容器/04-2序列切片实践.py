# -*- encoding: utf-8 -*-
# File : 04-2序列切片实践.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/18 21:29

"""
    有序字符串："你好伤wide心哈哈哈,哥茄大心伤我,哈哈的红红火火大牛啊 茄简直6到不行哥"
    使用学过的任何方式得到 "伤心大茄哥"
"""
init_str = '你好伤wide心哈哈哈,哥茄大心伤我,哈哈的红红火火大牛啊 茄简直6到不行哥'
result = (init_str.split(','))[1]
result = result.replace('我', '')

print(result[ : : -1])

# for i in range(len(result)):
#     print(result[ - i - 1 ], end='')