# -*- encoding: utf-8 -*-
# File : 02异常的传递.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/24 14:34

# 定义一个出现异常的方法 
def function_1():
    print('function1 start...')
    1 / 0
    print('function2 stop')

# 定义一个无异常的方法 调用上面的方法
def function_2():
    print('function2 start...')
    function_1()
    print('function2 stop')

# 定义一个方法 调用上面的方法
def main():
    try:
        function_2()
    except Exception as e:
        print(f'出现异常了 异常的信息是:{e}')

main()