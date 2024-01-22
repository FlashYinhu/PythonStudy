# -*- encoding: utf-8 -*-
# File : 02-02文件读取练习.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/22 19:10

"""
    给定测试文本文件 02-02.txt
    统计文件中单词 'the' 出现的次数
"""


# 方法1 读取全部内容为字符串 用count统计 the 和 THE的单词数量
# 这种方法是错误的 会将 theater 或者 OTHER 也识别为含有the 和 THE / The
f1 = open('./04文件/02-00.txt', 'r', encoding= 'UTF-8') 
content_str = f1.read()
count_the = content_str.count('the')
count_THE = content_str.count('THE')
count_The = content_str.count('The')
print(f'文件中单词the的数量为: {count_the + count_THE + count_The}')
f1.close

counts = 0
with open('./04文件/02-00.txt', 'r', encoding= 'UTF-8') as f2:
    for temp_line in f2:
        counts += temp_line.count('the')
        counts += temp_line.count('THE')
        counts += temp_line.count('The')
print(f'文件中单词the的数量为: {counts}')

# 方法2 按行读取内容 
print('============法2=============')
counts = 0
f3 = open('./04文件/02-00.txt', 'r', encoding= 'UTF-8')
for line in f3:
    line = line.strip() # 删除字符串前后的换行符和空格
    temp_list = line.split(' ') # 按空格分隔成单词列表
    # print(temp_list)
    for i in temp_list:
        i = i.strip('(),./') # 删除单词字符串前后冗余的符号
        if i == 'the':
            counts += 1
        elif i == 'THE':
            counts += 1
        elif i == 'The':
            counts += 1
print(f'文件中单词the的数量为: {counts}')
f3.close()
    # print(temp_list)
    # for i in temp_list
#     words = line.split(',')
#     for temp_str in words:
#         temp_str = temp_str.split(' ')
#         for words in temp_str:
#             if words == 'the' or 'THE':
#                 counts += 1


    