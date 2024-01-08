# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/8 19:39
import random
num = random.randint(1,10)
print(num)

guessnum = int(input("Your num(1~10):\n"))
if guessnum == num:
    print("1 Bingo!")
else:
    if guessnum < num:
        print("Too small!Try again!")
    else:
        print("Too Big!Try again!")

    guessnum = int(input("再次输入："))

    if guessnum == num:
        print("2 Bingo!")
    else:
        if guessnum < num:
            print("Too small!Try again!")
        else:
            print("Too Big!Try again!")

    guessnum = int(input("Your last chance:\n"))
    if guessnum == num:
        print("3 Bingo!")
    else:
        if guessnum < num:
            print("Too small!Game over!")
        else:
            print("Too Big!Game over!")
