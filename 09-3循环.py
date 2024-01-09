# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/9 14:34
# for循环/遍历循环（轮循）
# 语法 `for 变量 in 被处理的数据(序列类型)，内容可以被一个个取出`
# 序列类型包括 字符串，列表，元组等
# 和while循环不同 for 无法定义循环条件 只能从被处理的数据集中依次取出数据对其中的内容进进行处理
# 理论上来说， Python的for循环无法构建无限循环，被处理的数据不可能是无限大
name = 'kangyinhuaaaaaaaaaaaaaaa'
count = 0
for x in name:
    # 将name中的内容按个去除赋予x临时变量
    # 在循环体中对x进行处理
    if x == 'a':
        count += 1
    print(x, end='')
print()
print(f"字符串\"{name}\"中a的个数为{count}个")

# range语法
# 0~5
for r1 in range(5):
    print(r1, end='')
print()
# 5~10 不包括10
for r2 in range(5, 10):
    print(r2, end='')
print()
# 1~10 不包括10 数字之间间隔为2
for r3 in range(1, 10, 2):
    print(r3, end='')
print()

# 快速循环10次
# x = 0
for x in range(5):
    print(f"这是第{x}次打印")
# ↓↓↓↓↓↓ 不符合规范但实际上可以访问到
print(x)
# 正确写法应该在for循环前定义 x = 0 来访问for循环中的临时变量
