# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/9 16:14
"""
    函数是组织好的可以重复使用的用来实现特定功能的代码
    根据字符串的长度统计
"""
str1 = 'kangyinhu'
str2 = 'zhangrui'
str3 = 'xiaolei'
# 针对特定需求，编写可重复利用的代码，提高程序的复用性
# 减少代码的重复性，提高开发效率


def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度为{count}")


my_len(str1)
my_len(str2)
my_len(str3)

"""
    函数的定义
    def 函数名(传入参数):
        函数体
        return 返回值
"""


def say_hi():
    print("Hi, my name is kangyinhu!")
    return None


def add(a, b):
    # a, b为形式参数，函数可以没有参数，也可以有n个参数
    c = a + b
    print(f"{a}+{b}的计算结果是{c}\n")

# num1和num3为实际参数
num1 = int(input("Please input your numbers\n"))
num3 = int(input("Please input your numbers\n"))
add(num1, num3)


def help_buy(quantity, variety):
    feedback = f"没问题, 我帮你买了{quantity}个{variety}, 不用谢!!"
    return feedback
    # return之后的内容不执行
    # print("hhhhhhhhh")


v = input('要我买什么东西?\n')
q = int(input('买几个?\n'))
print(help_buy(q, v))
# 函数返回值的None类型
result = say_hi()
print('无返回值函数返回的内容是', result, '返回的类型是', type(result))

"""
    在if判断中，None等同于False
"""


def check_age(age):
    if age >= 18:
        return "SUCESS"
    #else:
        #return None


myage = int(input("Please input your age:\n"))
result = check_age(myage)
if result:
    print('You are an adult!')
else:
    print('You are a chlidren!')

# 用于声明无初始内容的变量
date = None

# 函数的说明文档，辅助理解函数的作用，写在函数题之前


def myfunction(a, b, c, d, e):
    """
    函数说明, 接收5个参数
    :param a: 形式参数a的说明
    :param b: 形式参数b的说明
    :param c: 形式参数c的说明
    :param d: 形式参数d的说明
    :param e: 形式参数e的说明
    :return: 返回值的说明
    """

    params = f"接收到的参数为{a}, {b}, {c}, {d}, {e}"
    return params


# 鼠标悬停在函数上会显示说明文档的内容
myresult = myfunction(1, 2, 3, 4, 5)
print(myresult)

