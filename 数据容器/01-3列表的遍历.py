# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/10 17:24

info = ['kangyinhu', 24, 187.56, True, [1, 2, 3]]
print(len(info))

# 遍历列表 if 不可以自定义循环条件
# 理论上不可以无限循环，因为被遍历的内容不是无限的
# 适用于遍历数据容器或者简单的固定次数循环的场景
for i in range(len(info)):
    print(info[i])
print()

# 遍历列表 while 可以自定义循环条件
# 可以通过控制条件实现无限循环
# 适用于任何想要实现循环的场景
length = len(info)
index = 0
while index < length:
    print(info[index])
    index += 1
