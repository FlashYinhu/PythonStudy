# 字符串定义方式
str1 = 'kang' # 单引号定义法
str2 = "yin"   # 双引号定义法
str3 = """hu""" # 三引号定义法
# 在字符串内包含双引号
str4 = '"zhang"'
# 在字符串内包含单引号
str5 = "'rui'"
# 转义字符
str6 = "\"hhh\""
print(str6)

# 字符转的拼接
name = "kangyinhu"
age = 24
height = 187.5
# 字面量和变量进行拼接 注意!!!字符串不能通过 + 和其他数据类型进行拼接
print("My name is " + name)
# 字符串格式化 %表示占位 s表示将变量变成字符串放入占位的地方
# s表示将变量变成字符串放入占位的地方
# d表示将变量变成整数放入占位的地方
# f表示将变量变成浮点数放入占位的地方
introduction = "Hi! My name is %s, i'm %d years old,my height is %f cm" %(name,age,height)
print(introduction)

"""
    格式化的精度控制,使用辅助符号m,n控制数据的宽度和精度
    -m 控制宽度,很少使用,宽度小于数字自身时不生效
    -n 控制小数点,要求是数字,会进行小数的四舍五入
"""
print("我的身高是%3.2fcm" %height)

# 快速格式化字符串的方式,不限数据类型不做精度控制原样输出,适合对精度没有要求的时候快速使用
print(f"My name is {name},i'm {age} years old and my height is {height}cm")

# 对表达式进行格式化
# 表达式:一条具有明确具体结果的代码语句
print("2 * 4的结果是:%d" % (2 * 4))
print(f"3 * 6的结果是:{3 * 6}")
print("字符串在python中的数据类型是: %s" % (type('str')))
