# -*- encoding: utf-8 -*-
# File : 02文件的读取.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/22 17:35

"""
    打开 关闭 读 写
    打开 open函数(name, code, encoding) 
        name - 文件名字符串 可以包含文件具体路径
        mode - 设置文件的打开模式(访问模式): 只读 写入 追加等
            r w a :read write add
        encoding - 编码格式(推荐UTF-8)
"""

# 打开文件 注意 encoding不是第三个参数 使用关键字传参
import time


f = open('./test.txt', 'r', encoding= 'UTF-8')
print(type(f))

# 读取文件 - read([num])  // num表示从文件中读取的数据长度(单位是字节) 如果没有传入num就表示读取文件中的所有数据
print(f'读取11个字节的结果是: {f.read(11)}')
str1 = f.read() # 多次调用read 后续的read会从上一个read的结尾处开始读取
print(f'读取剩余文件的所有内容的结果是: {str1}')

# 读取文件 - readLines() 读取文件的全部行并分装到一个列表中
# 每一行的数据为一个元素
lines = f.readlines()
print(f'lines对象的类型是: {type(lines)}')
print(f'lines对象的内容是: {lines}')

# 读取文件 - readLine() 一次读取一行内容
f2 = open('./test.txt', 'r', encoding= 'UTF-8')
line1 = f2.readline()
line2 = f2.readline()
line3 = f2.readline()
print(f'line1的类型是: {type(line1)}')
print(f'line1的内容是: {line1}')
print(f'line2的内容是: {line2}')
print(f'line3的内容是: {line3}')

# for循环读取文件对象
# for temp_line in open('./test.txt', 'r'):
#     print(temp_line)

f3 = open('./test.txt', 'r', encoding= 'UTF-8')
for line in f3:
    print(line)


# 关闭文件对象 如果不关闭文件 文件会一直被python程序占用
f.close()
f2.close()
f3.close()

# with open 语法对文件进行操作 可以在完成操作后自动关闭cloes文件 避免遗忘掉close方法
line_id = 1
with open('./test.txt', 'r', encoding='UTF-8') as f4:
    for line in f4:
        print(f'第{line_id}行的数据是: {line}')
        line_id += 1
