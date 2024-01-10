# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/8 17:26
name1 = "kangyinhu"
age1 = 25
name2 = "zhangrui"
age2 = 24
if age1 == 25:
    print(name1)
    if age1 >= 18:
        print("i'm an adult.")

print("kangyinhuhaoshuai")

# str1 = input("please input your age\n")
# age = int(str1)
age = int(input("Please input your age:\n"))
if age >= 18:
    print("You are an adlut, please pay $10")
else:
    if age <= 14:
        print("You are a children, you are free!")
print("Have fun!")

# elif 的判断是互斥且有顺序的
# else 可以不写 不满足时不采取任何操作
name = input("Plese input your name:\n")
if name == "kangyinhu":
    print("You are our VIP!")
elif name == "zhangrui":
    print("You are our VIP!")
elif name == "hhh":
    print("You are our VIP!")
else:
    print("Sorry, you are not our VIP!")

# 简化代码
if input("Please input your namn\n") == "kangyinhu":
    print("You are our VIP!")

# 小游戏 猜数字
num = 6
if int(input("please input your number:\n")) == 6:
    print("666!")
elif int(input("Wrong!please input your number again:\n")) == 6:
    print("good!")
elif int(input("Sorry!please input your number again:\n")) == 6:
    print("6!")
else:
    print("Gameover!")

# 嵌套使用
epage = int(input("Please input your age:\n"))
if 18 <= epage < 30:
    if float(input("请输入你就职的时长:\n")) > 2:
        print("恭喜你，年终奖有你一份！")
    elif int(input("您的入职时间不足，请输入你的行政级别:\n")) > 3:
        print("恭喜您，年终奖有你一份")
    else:
        print("对不起，您没有年终奖")
else:
    print("对不起小弟弟你走错片场了")

