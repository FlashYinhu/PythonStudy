# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/8 19:53
"""
    循环的实际应用：
    循环广告牌 批量修图 视频轮播 音乐轮播 大喇叭喊话 动态壁纸 视频监控
"""
import random

num = 1
sum = 0
while num <= 100:
    print(num)
    sum += num
    num += 1
print("1+2+3+...+98+99+100 =", sum)

print("=====下面是猜数字=====")
randomnum = random.randint(1, 100)

# My code:
# count = 1
# guessnum = int(input("GuessNumber:"))
# while guessnum != randomnum:
#     if guessnum < randomnum:
#         guessnum = int(input("Too small!"))
#         count += 1
#     else:
#         guessnum = int(input("Too big!"))
#         count += 1
# print(f"恭喜你猜对了!,你一共猜了{count}次！")

# 利用bool变量进行
flag = True
count = 0
while flag:
    guessnum2 = int(input("Your number:"))
    count += 1
    if guessnum2 == randomnum:
        print(f"Bingo!{count}")
        flag = False
    else:
        if guessnum2 < randomnum:
            print("Too small!")
        else:
            print("Too big!")
