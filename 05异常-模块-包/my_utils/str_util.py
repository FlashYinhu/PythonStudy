# -*- encoding: utf-8 -*-
# File : str_util.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/24 15:44

# 传入字符串 反转返回
def str_reverse(s: str) -> str:
    """
    功能是将字符串完成反转
    :param s:将被反转的字符串
    :return: 反转后的字符串
    """
    # list = []
    # for i in range(len(s)):
    #     list.append(s[- i - 1])
    # return str(list)
    return s[ : : -1 ]

# 传入 x y s 按照下标进行字符串切片
def substr(s: str, x: int, y:int):
    """
    功能是按照给定的下标完成字符串的切片
    :param s: 即将被切片的字符串
    :param x: 切片开始的下标
    :param y: 切片结束的下标
    """
    str_former = s[ : x: 1]
    mystr = s[x: y: 1]
    str_later = s[ y: :1]
    print(f'分割后的字符串为 {str_former}|{mystr}|{str_later}')

if __name__ == '__main__':
    result = str_reverse('kangyinhu')
    print(result, type(result))
    substr('kangyinhu', 4, 7)