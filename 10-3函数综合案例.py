# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/9 19:22
money = 5000000.00
name = None
flag = True


def main_menu():
    while flag:
        print('========ATM SYSTEM=========')
        print('1. 查询余额')
        print('2. 存款')
        print('3. 取款')
        print('4. 退出')
        print('===========================')
        i = int(input('PLEASE SELECT THE ACTION YOU WANT TO TAKE(1~4)\n'))
        if i == 1:
            check_balance()
            continue
        elif i == 2:
            deposit()
            continue
        elif i == 3:
            withdrawal()
            continue
        elif i == 4:
            print('WELCOME TO YOUR NEXT VISIT!')
            break
        else:
            print('YOUR ENTRY IS INVALID!! THE SYSTEM HAS EXITED!!')
            break


def check_balance():
    print(f'Your current balance is {money}$\n')


def deposit():
    global money
    dep_money = float(input('PLEASE ENTER YOUR DEPOSIT AMOUNT\n'))
    money += dep_money
    print(f'Deposit money successfully!You just deposit {dep_money}$')
    print(f'Your current balance is {money}$\n')


def withdrawal():
    global money
    with_money = float(input('PLEASE ENTER YOUR DEPOSIT AMOUNT\n'))
    money -= with_money
    print(f'Withdraw money successfully!You just withdraw {with_money}$')
    print(f'Your current balance is {money}$\n')


name = input('PLEASE ENTER YOUR NAME:\n')
main_menu()
