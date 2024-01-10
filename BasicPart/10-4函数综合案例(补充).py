# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/10 10:57

money = 5000000
name = None
name = input("PLEASE INPUT YOUR NAME:\n")


# 查询
def query(show_header):
    if show_header:
        print('------QUERY BALANCE-------')
    print(f'WELCOME, {name}!, YOUR BALANCE IS {money}$')


# 存
def deposit(num):
    global money
    money += num
    print('------DEPOSIT MONEY-------')
    print(f'{name}, YOU DEPOSIT MONEY {num}$ SUCCESSFULLY!')
    query(False)


# 取
def withdraw(num):
    global money
    money -= num
    print('------WITHDRAW MONEY------')
    print(f'{name}, YOU WITHDRAW MONEY {num}$ SUCCESSFULLY!')
    query(False)


# MENU
def main():
    print('========ATM SYSTEM=========')
    print(f'WELCOME! {name},PLEASE SELECT THE NUMBER')
    print('1. QUERY')
    print('2. DEPOSIT')
    print('3. WITHDRAW')
    print('4. EXIT')
    print('===========================')
    return input("PLEASE INPUT YOUR CHOISE")


# 设置无限循环
while True:
    keyboard_input = main()
    if keyboard_input == '1':
        query(True)
        continue # continue 继续下一次循环
    elif keyboard_input == '2':
        num = int(input("PLEASE INPUT THE NUMBER YOU WANT TO DEPOSIT: "))
        deposit(num)
        continue
    elif keyboard_input == '3':
        num = int(input("PLEASE INPUT THE NUMBER YOU WANT TO WITHDRAW: "))
        withdraw(num)
        continue
    else:
        print("EXIT!")
        break
