# -*- coding:utf-8 -*-
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date : 2024/1/10 15:33
"""
    在python中，如果将函数定义为class类的成员，则称该函数为方法
    方法和函数功能一样，都有传入参数和返回值，只是方法的使用格式不同
    方法的使用：
        kangyinhu = Kangyinhu()
        num = kangyinhu.info(name)
"""
# 查找元素在列表中的下标
name = ['kangyinhu', 'zhangrui', 'xiaolei']
print(name)
print(f'kangyinhu在列表中的下标索引是:{name.index('kangyinhu')}\n')

# 查找不存在的元素会报错
# print(name.index('zhangsan'))

# 修改特定下标索引的值
print("将zhangrui的姓名修改为zhangdapao")
name[1] = 'zhangdapao'
print(f'修改后的列表为:{name}\n')

# 在指定下标位置插入新元素
print('在kangyinhu后面插入zhangsan')
name.insert(1, 'zhangsan')
print(f'修改后的列表为:{name}\n')

# 在列表中进行元素的追加，将指定元素追加到列表的尾部
print('在列表的尾部追加单个新的元素')
name.append('lisi')
name.append('wangwu')
print(f'修改后的列表为:{name}\n')

# 在列表后追加一批元素，将其他数据容器作为参数传入，将该数据容器中的元素
# 全部追加到需要的列表中
print('在列表的尾部批量追加新的元素')
name_extend = ['zhaoqian', 'sunli', 'zhouwu', 'zhengwang', 'xiaoshang']
name.extend(name_extend)
print(f'修改后的列表为:{name}\n')

# 元素的删除del
print('del指定列表元素下标[0]删除列表中的元素\'kangyinhu\'')
del name[0]
print(f'修改后的列表为:{name}\n')

# 元素的删除pop:取出列表中的元素
print('pop指定列表元素下标[2]删除列表中的元素\'xiaolei\'')
temp = name.pop(2)
print(f'修改后的列表为:{name}')
print(f'取出的元素为{temp}\n')

# 删除某元素在列表中第一个匹配项
print('删除元素\'zhangdapao\'在列表中第一个匹配项')
name.remove('zhangdapao')
print(f'修改后的列表为:{name}\n')

# 清空列表
print('通过clear方法清空列表')
name.clear()
print(f'修改后的列表为:{name}\n')

# 统计列表中某元素的数量
name.append('zhouwu')
name.extend(name_extend)
print('统计\'zhouwu\'在列表中的数量')
print(f'目前的列表为:{name}')
print('列表中\'zhouwu\'的数量为%d\n' % (name.count('zhouwu')))

# 统计列表中全部的元素数量
print('列表的元素数量为:%d\n' % len(name))

# 小练习
my_numbers = [21, 25, 21, 23, 22, 20]
my_numbers.append(31)
numbers_add = [29, 33, 30]
my_numbers.extend(numbers_add)
num1 = my_numbers.pop(0)
num2 = my_numbers.pop(len(my_numbers) - 1)
myindex = my_numbers.index(31)
print(f'{my_numbers},\n{num1}, {num2}')
