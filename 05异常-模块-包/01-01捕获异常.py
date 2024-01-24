# -*- encoding: utf-8 -*-
# File : 01-01捕获异常.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/22 20:48

"""
    对于可能出现的bug 进行提前准备和处理
        - 程序会因为bug停止
        - 对bug进行提醒 程序继续运行
    作用在于 提前假设某处会出现异常 做好提前准备 当真的出现异常的时候 可以有后续手段
    try:
        可能发生异常的代码
    except:
        如果出现异常执行的代码
"""

# 基本捕获语法
try:
    fr = open('./05异常-模块-包/01-00.txt', 'r', encoding= 'UTF-8')
    mystr = fr.readlines()
    print(f'打开文件成功!\n文件的内容是:\n{mystr}')
except:
    print('文件不存在！open的模式更改为写模式！')
    fw = open('./05异常-模块-包/01-00.txt', 'w', encoding= 'UTF-8')
    fw.write('Hello! My name is kangyinhu!')
    fw.close()
print()

# 捕获指定的异常
try:
    print(name)
    # 1 / 0
except NameError as e:
    print('出现了变量未定义的异常')
    print(e, type(e))

# 捕获多个异常
try:
    1 / 0
    # print(kyh)
except (NameError, ZeroDivisionError) as e:
    print('出现了变量未定义或除0的异常错误\n')

# 捕获所有异常
try: 
    # 1 / 0 
    # print(zr)
    f = open('./xxx.txt', 'r', encoding= 'UTF-8')
# Exception为顶级异常
except Exception as e:         # 这句话就等于 except: 
    print(f'出现了异常, 异常的类型是:{type(e)}, 异常的内容是:{e}\n')

# 异常的else和finally
try: 
    print('=====准备打开文件=====')
    fr = open('./asdasd.txt', 'r', encoding= 'UTF-8')
except Exception as e: 
    print(f'出现了异常, 异常的类型是:{type(e)}, 异常的内容是:{e}')
else:                           # 没有异常时执行
    print('执行try-else, 程序没有异常!')
finally:                        # 无论异常与否都要执行的代码, 例如关闭文件
    fr.close()
    print(f'文件打开失败, fr已关闭!')
