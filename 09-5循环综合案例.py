# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/9 16:02
import random
"""
    某公司，账户余额有1W元，给20名员工发工资。
    员工编号从1到20，从编号1开始，依次领取工资，每人可领取1000元。
    领工资时，财务判断员工的绩效分(1-10) (随机生成)，如果低于5，不发工资。
    换下一位如果工资发完了，结束发工资
"""
companyAccount = 10000
for emp in range(1, 21):
    if companyAccount == 0:
        print("余额不足，不足以发工资，转至下月结算")
        break
    pf = random.randint(1, 10)
    if pf < 5:
        print(f'员工{emp}， 绩效分为{pf}，绩效太低，没有工资，下一位')
        continue
    else:
        companyAccount -= 1000
        print(f"向员工{emp}发放工资1000元，账户余额{companyAccount}")


