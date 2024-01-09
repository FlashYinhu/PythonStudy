# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/9 15:40
# continue: 中断本次循环
print("continue关键字的用法")
for i in range(1, 6):
    if i == 3:
        print("第三次我不想hh")
        continue
    print('hhhhhh')
print()

print('输出1~100中可以被4整除的数字')
print('我只想知道前10个')
mycount = 0
for i in range(1, 101):
    if i % 4 == 0:
        mycount += 1
        print(f"{i} ", end='')
    if mycount == 10:
        break
