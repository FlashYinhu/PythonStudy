"""
    规则1:内容限定:中英文,数字,下划线,不能以数字开头
    错误示范: 1_name="zhangrui"
    错误师范:name_1!="zhangsan"
"""
name_ = "zhangsan"
_name = "zhangsan"
name_1 = "zhangsan"

# 规则2 大小写敏感
Age = 12
age = 24

# 规则3 不可以使用关键字
# 错误的示例class = 1
Class = 1
# 错误的示例def = 2
Def = 2

"""
    标识符命名的规范  变量,类,方法
    变量:
    - 明了,见名知意 : name = "kangyinhu" age = 24
    - 下划线命名法: first_num student_nickname
    - 英文字母全小写
"""